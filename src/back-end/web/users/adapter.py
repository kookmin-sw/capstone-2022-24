"""Adapter of Social Account model for social login"""
import requests
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field, perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import exceptions, status
from rest_framework.response import Response

from users.models import User
from django.conf import settings


class UserAdapterSupporter:

    def __init__(self, settings_file):
        self.conf = settings_file
        self.load_oauth2_setting()
        self.supported_providers = None

    def get_host(self):
        return f"{self.conf.APP_HOST}:{self.conf.APP_PORT}"

    def load_oauth2_setting(self):
        self.supported_providers = self.conf.SOCIALACCOUNT_PROVIDERS

    def get_provider_app(self, provider):
        return self.supported_providers.get(provider).get("APP")

    def get_provider_id(self, provider):
        return self.get_provider_app(provider).get("client_id")

    def get_provider_secret(self, provider):
        return self.get_provider_app(provider).get("client_secret")


class UserAdapter(DefaultSocialAccountAdapter):
    """Custom Social Account Adapter"""

    def __init__(self, request=None):
        super().__init__(request)
        self.supporter = UserAdapterSupporter(settings)

    def logged_in_with(self, sociallogin, expected):
        """True if user sign in with <expected> application else False"""
        return sociallogin.account.provider == expected

    def disconnect(self, sociallogin):
        """Detach provider account from Ongot service"""
        if self.logged_in_with(sociallogin, "naver"):
            base_url = "https://nid.naver.com/oauth2.0/token"
            params = f"?grant_type=delete&client_id={self.supporter.get_provider_id('naver')}" \
                     f"&client_secret={self.supporter.get_provider_secret('naver')}&access_token={sociallogin.token}"
            response = requests.get(base_url + params)
            if response.json().get("result") != "success":
                raise exceptions.ParseError("네이버 로그인 연동 해제 실패")
        elif self.logged_in_with(sociallogin, "google"):
            url = f"https://accounts.google.com/o/oauth2/revoke?token={sociallogin.token}"
            requests.get(url)
            response = requests.post('https://oauth2.googleapis.com/revoke',
                                     params={'token': sociallogin.token},
                                     headers={'content-type': 'application/x-www-form-urlencoded'})
            if response.status_code != 200:
                raise exceptions.ParseError("구글 로그인 연동 해제 실패")

    def pre_social_login(self, request, sociallogin):
        """Check social account details (Called just before sign in/up)
        1. validate social account, return
        2. social account doesn't have full information needed in service, return
        3. link user account to social account
        """
        # 1. validate login
        # 1.1 social account already exists
        if sociallogin.is_existing:
            return
        # 1.3 social login user already exists
        if sociallogin.user.id:
            return
        # 2. social account has no email/birthyear/mobile unknown, return
        # 2-1. with naver
        if self.logged_in_with(sociallogin, "naver"):
            response = sociallogin.account.extra_data
            if "name" not in response:
                messages.error(request, "name is not provided")
            elif "email" not in response:
                messages.error(request, "email is not provided")
            elif "birthyear" not in response:
                messages.error(request, "birthday is not provided")
            elif "mobile" not in response:
                messages.error(request, "Phone number is not provided")
            else:
                return
            self.disconnect(sociallogin)
            raise ImmediateHttpResponse(redirect("/login/naver"))
        # 2-2. with google
        elif sociallogin.account.provider == "google":
            if "email" not in sociallogin.account.extra_data:
                messages.error(request, "email is not provided")
            # elif "birthday" not in sociallogin.account.extra_data:
            #     messages.error(request, "birthday is not provided")
            #     raise ImmediateHttpResponse(redirect("/"))
            # elif "mobile" not in sociallogin.account.extra_data:
            #     messages.error(request, "Phone number is not provided")
            #     raise ImmediateHttpResponse(redirect("/"))
            else:
                return
            self.disconnect(sociallogin)
            raise ImmediateHttpResponse(redirect("/login/google"))

        # 3. link auth user account to social account
        try:
            email = sociallogin.account.extra_data["email"]
            user = User.objects.get(email__iexact=email)
            sociallogin.connect(request, user)  # linking account
            perform_login(request, user, 'none')
        except User.DoesNotExist:  # -> create a new user
            pass

    def populate_user(self, request, sociallogin, data):
        """Set fields of the user object"""
        response = sociallogin.account.extra_data

        # Naver: if user sign in with naver account
        if self.logged_in_with(sociallogin, "naver"):
            email = data.get("email")
            uid = response.get("id")
            temp_nickname = uid[:8]
            name = response.get("name")
            cell_phone_number = response.get("mobile")
            birth_year = response.get("birthyear")
            birthday = birth_year + "-01-01"
        # Google: if user sign in with google account
        elif self.logged_in_with(sociallogin, "google"):
            email = data.get("email")
            uid = response.get("id")
            temp_nickname = uid[:8]
            name = response.get("name")
            birthday = "1900-01-01"  # TODO
            cell_phone_number = "000-0000-0000"  # TODO
            # api_key = settings.SOCIALACCOUNT_PROVIDERS["google"]["APP"]["key"]
            # request_base = f"https://people.googleapis.com/v1/people/{uid}"
            # url = request_base += ?personFields=phoneNumbers,birthdays&key={api_key}&access_token={sociallogin.token}"
            # birthday_and_phone_numbers = requests.get(url).json()
            # birthday_meta = birthday_and_phone_numbers.get("birthdays")
            # birthday = f"{birthday_meta.get('year')}-{birthday_meta.get('month')}-{birthday_meta.get('day')}"
        user = sociallogin.user
        user_field(user, "nickname", temp_nickname)
        user_field(user, "name", name)
        user_field(user, "email", email)
        user_field(user, "cell_phone_number", cell_phone_number)
        user_field(user, "birthday", birthday)
        return user

    def save_user(self, request, sociallogin, form=None):
        super().save_user(request, sociallogin, form)
        raise ImmediateHttpResponse(Response(status=status.HTTP_301_MOVED_PERMANENTLY, headers={"Location": "http://localhost:3000/register/"}, data={"access_token": sociallogin.token}))
