"""drf-spectacular api schemas"""
from drf_spectacular.utils import OpenApiExample

VIDEO_CATEGORY_NOT_MATCH_EXAMPLE = OpenApiExample(
    response_only=True, name="Wrong Video ID", value={"detail": "작품 종류와 맞지않은 작품 ID입니다."}
)

VIDEO_NOT_FOUND_EXAMPLE = OpenApiExample(response_only=True, name="Not Found", value={"detail": "존재하지 않은 작품입니다."})
