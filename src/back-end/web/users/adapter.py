"""Adapter of Social Account model for social login"""
from allauth.account.utils import user_field
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect
from users.models import User


class UserAdapter(DefaultSocialAccountAdapter):
    """Custom Social Account Adapter"""

    def pre_social_login(self, request, sociallogin):
        """Check social account details (Called just before sign in/up)
        1. social account already exists, return
        2. social account doesn't have full information needed in service, return
        3. link user account to social account
        """

        # 1. social account already exists
        if sociallogin.is_existing:
            return

        # 2. social account has no email/birthyear/mobile unknown, return
        # 2-1. with naver
        if sociallogin.account.provider == "naver":
            response = sociallogin.account.extra_data
            if "name" not in response:
                messages.error(request, "name is not provided")
                raise ImmediateHttpResponse(redirect("/"))
            if "email" not in response:
                messages.error(request, "email is not provided")
                raise ImmediateHttpResponse(redirect("/"))
            if "birthyear" not in response:
                messages.error(request, "birthday is not provided")
                raise ImmediateHttpResponse(redirect("/"))
            if "mobile" not in response:
                messages.error(request, "Phone number is not provided")
                raise ImmediateHttpResponse(redirect("/"))
        # 2-2. with google
        elif sociallogin.account.provider == "google":
            print(sociallogin.account.extra_data)
            # if "email" not in sociallogin.account.extra_data:
            #     messages.error(request, "email is not provided")
            #     raise ImmediateHttpResponse(redirect("/"))
            # if "birthday" not in sociallogin.account.extra_data:
            #     messages.error(request, "birthday is not provided")
            #     raise ImmediateHttpResponse(redirect("/"))
            # if "mobile" not in sociallogin.account.extra_data:
            #     messages.error(request, "Phone number is not provided")
            #     raise ImmediateHttpResponse(redirect("/"))

        # 3. link auth user account to social account
        try:
            email = sociallogin.account.extra_data["email"]
            user = User.objects.get(email__iexact=email)
            sociallogin.connect(request, user)  # linking account
            user.set_password(None)  # optional, so user can't login with password
            user.save()
            return
        except User.DoesNotExist:
            # if user not found then let allauth to create a new user
            return

    def populate_user(self, request, sociallogin, data):
        """Set fields of the user object"""
        response = sociallogin.account.extra_data
        print(response)

        # Naver: if user sign in with naver account
        if sociallogin.account.provider == "naver":
            email = data.get("email")
            temp_nickname = response.get("id")[:8]
            name = response.get("name")
            cell_phone_number = response.get("mobile")
            birth_year = response.get("birthyear")
            birthday = birth_year + "-01-01"
        # Google: if user sign in with google account
        elif sociallogin.account.provider == "google":
            email = data.get("email")
            temp_nickname = response.get("id")[:8]
            name = response.get("name")
            cell_phone_number = response.get("contact")
            birthday = response.get("birthday")

        user = sociallogin.user
        user_field(user, "nickname", temp_nickname)
        user_field(user, "name", name)
        user_field(user, "email", email)
        user_field(user, "cell_phone_number", cell_phone_number or "000-0000-0000")
        user_field(user, "birthday", birthday)
        return user
