"""APIs of users application"""
from allauth.account import app_settings
from allauth.account.utils import complete_signup
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.utils import get_username_max_length
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.serializers import JWTSerializer
from dj_rest_auth.views import LoginView, LogoutView
from django.conf import settings
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.views import TokenRefreshView
from users.exceptions import NicknameValidationException
from users.models import User
from users.schemas import TOKEN_WITH_USER_LOGIN_SUCCESS_RESPONSE_EXAMPLE
from users.serializers import (
    GoogleLoginSerializer,
    NaverLoginSerializer,
    NicknameSerializer,
    ProfileImageSerializer,
    UserSignUpVerifySerializer,
)


@extend_schema(
    tags=["Priority-1", "User"],
    operation_id="네이버 로그인",
    parameters=[
        OpenApiParameter(
            name="set-cookie ",
            description="ongot-token={{Access Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=39600;",
            type=str,
            location=OpenApiParameter.COOKIE,
            response=True,
        ),
        OpenApiParameter(
            name="set-cookie",
            description="ongot-refresh-token={{Refresh Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=54000;",
            type=str,
            location=OpenApiParameter.COOKIE,
            response=True,
        ),
    ],
    responses={
        200: OpenApiResponse(
            response=JWTSerializer, description="네이버 로그인 성공", examples=[TOKEN_WITH_USER_LOGIN_SUCCESS_RESPONSE_EXAMPLE]
        )
    },
)
class NaverLoginView(SocialLoginView):
    """Login with Naver account"""

    adapter_class = NaverOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = NaverLoginSerializer
    callback_url = f"{settings.APP_HOST}:{settings.APP_PORT}"


@extend_schema(
    tags=["Priority-1", "User"],
    operation_id="구글 로그인",
    request=inline_serializer(
        name="GoogleOAuth2LoginSerializer",
        fields={
            "accessToken": serializers.CharField(),
        },
    ),
    parameters=[
        OpenApiParameter(
            name="set-cookie ",
            description="ongot-token={{Access Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=39600;",
            type=str,
            location="cookie",
            response=True,
        ),
        OpenApiParameter(
            name="set-cookie",
            description="ongot-refresh-token={{Refresh Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=54000;",
            type=str,
            location="cookie",
            response=True,
        ),
    ],
    responses={
        200: OpenApiResponse(
            response=JWTSerializer, description="구글 로그인 성공", examples=[TOKEN_WITH_USER_LOGIN_SUCCESS_RESPONSE_EXAMPLE]
        )
    },
)
class GoogleLoginView(SocialLoginView):
    """Login with Google account"""

    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = GoogleLoginSerializer
    callback_url = f"{settings.APP_HOST}:{settings.APP_PORT}"


@extend_schema(
    tags=["Priority-1", "User"],
    operation_id="회원 가입",
    request=inline_serializer(
        name="SignUpRequestSerializer",
        fields={
            "nickname": serializers.CharField(
                max_length=get_username_max_length(),
                min_length=app_settings.USERNAME_MIN_LENGTH,
                required=app_settings.USERNAME_REQUIRED,
                validators=[UniqueValidator(queryset=User.objects.all())],
            ),
            "profileImageUrl": serializers.URLField(required=False),
        },
    ),
    responses={
        200: OpenApiResponse(
            description="회원 가입 성공",
            response=inline_serializer(
                name="VerifyUserSerializer",
                fields={
                    "nickname": serializers.CharField(
                        max_length=get_username_max_length(),
                        min_length=app_settings.USERNAME_MIN_LENGTH,
                        required=app_settings.USERNAME_REQUIRED,
                        validators=[UniqueValidator(queryset=User.objects.all())],
                    ),
                    "profileImageUrl": serializers.URLField(required=False),
                    "name": serializers.CharField(),
                    "email": serializers.EmailField(),
                    "isVerified": serializers.BooleanField(),
                },
            ),
        )
    },
)
class SignUpView(CreateAPIView):
    """Sign up with nickname(required) and profile image(optional)"""

    serializer_class = UserSignUpVerifySerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """Save user's nickname & profile"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = self.get_response_data(user)
        return Response(data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(self.request, user, settings.ACCOUNT_EMAIL_VERIFICATION, settings.ACCOUNT_SIGNUP_REDIRECT_URL)
        return user

    def get_response_data(self, user):
        """Get serializer + other user context data"""
        return {
            "name": user.name,
            "nickname": user.nickname,
            "profile_image_url": user.profile_image_url,
            "email": user.email,
            "is_verified": user.is_verified,
        }


@extend_schema(
    tags=["Priority-1", "User"],
    operation_id="닉네임 사용 가능 여부 확인",
    parameters=[OpenApiParameter("nickname", NicknameSerializer)],
    responses={
        200: OpenApiResponse(
            description="사용 가능한 닉네임",
            response=inline_serializer(
                name="AvailableNickname",
                fields={"code": serializers.CharField(), "message": serializers.CharField()},
            ),
        ),
        400: OpenApiResponse(
            description="올바르지 않은 형식",
            response=inline_serializer(
                name="InvalidFormatNickname",
                fields={"code": serializers.CharField(), "message": serializers.CharField()},
            ),
        ),
        409: OpenApiResponse(
            description="이미 존재하는 닉네임",
            response=inline_serializer(
                name="DuplicatedNickname",
                fields={"code": serializers.CharField(), "message": serializers.CharField()},
            ),
        ),
    },
)
class ValidateNicknameView(GenericAPIView):
    """Validation about nickname when user sign up"""

    queryset = User.objects.all()
    serializer_class = NicknameSerializer
    lookup_field = "nickname"

    def get(self, request):
        """Validate nickname

        code: validation keyword (English)

        message: validation details (Korean)
        """
        nickname = request.query_params.get("nickname", None)
        serializer = NicknameSerializer(data={"nickname": nickname})
        try:
            # validate nickname
            if serializer.is_valid(raise_exception=True):
                # not verified user
                # if request.user.is_verified:
                #     return Response(
                #         data=self.get_response_data(code="already_set", message="이미 닉네임을 설정했습니다."),
                #         status=status.HTTP_403_FORBIDDEN,
                #     )
                # SUCCESS: valid format + verified user
                return Response(
                    data=self.get_response_data(code="available_nickname", message="사용 가능한 닉네임입니다."),
                    status=status.HTTP_200_OK,
                )
            # other cases
            return Response(
                data=self.get_response_data(code="invalid_nickname", message="유효하지 않은 닉네임입니다."),
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as error:
            response = NicknameValidationException(error)
            return Response(response.get_full_details(), status=response.status_code)

    def get_response_data(self, code="success", message=None):
        """Make response data with code, message parameter"""
        response = {}
        if code:
            response["code"] = code
        if message:
            response["message"] = message
        return response


@extend_schema(tags=["Deprecated"], operation_id="프로필사진 사용 가능 여부 확인")
class ValidateProfileImageView(GenericAPIView):
    """Validation about profile image to use"""

    queryset = User.objects.all()
    serializer_class = ProfileImageSerializer


@extend_schema_view(
    operation_id="프로필사진 업로드",
    post=extend_schema(tags=["Deprecated"], operation_id="프로필사진 업로드", description="Upload in Back-end and set URL"),
    patch=extend_schema(
        tags=["Priority-1", "User"], operation_id="프로필사진 URL 변경", description="Set url(uploaded in Front-End)"
    ),
)
class ProfileImageUploadView(CreateAPIView, UpdateAPIView):
    """Upload profile image of user"""

    queryset = User.objects.all()
    serializer_class = ProfileImageSerializer
    http_method_names = ["post", "patch"]

    def get_object(self):
        """Get request user"""
        # Get login user
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        """Upload profile image in BACK-END Server"""
        # parser_classes = (MultiPartParser, FormParser)
        # Not implemented yet
        # Upload image file in S3 from multipart/form-data
        return super().create(request, args, kwargs)


@extend_schema(tags=["Priority-1", "User"], operation_id="회원 탈퇴 가능 여부 확인")
class ValidateWithdrawalView(GenericAPIView):
    """Validation about user's withdrawal using whether to join groups"""

    # TODO


@extend_schema(tags=["Priority-1", "User"], operation_id="회원 탈퇴")
class UserWithdrawalView(GenericAPIView):
    """Withdrawal by checking whether to delete"""

    # TODO


@extend_schema(
    tags=["User"],
    operation_id="일반 로그인",
    responses={
        200: OpenApiResponse(
            response=JWTSerializer, description="일반 로그인 성공", examples=[TOKEN_WITH_USER_LOGIN_SUCCESS_RESPONSE_EXAMPLE]
        )
    },
)
class GeneralLoginView(LoginView):
    """Inherit class of dj_rest_auth LoginView"""


@extend_schema(tags=["User"], operation_id="통합 로그아웃")
class GeneralLogoutView(LogoutView):
    """Inherit class of dj_rest_auth LoginView"""


@extend_schema(tags=["Priority-1", "User"], methods=["post"], operation_id="토큰 재발급")
class RefreshTokenView(TokenRefreshView):
    """Get refresh token using dj_rest_auth module"""
