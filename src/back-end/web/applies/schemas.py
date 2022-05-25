"""Swagger schema examples"""
from drf_spectacular.utils import OpenApiExample

GROUP_APPLY_POST_EXAMPLE = [
    OpenApiExample(
        name="Success example (201)",
        response_only=True,
        value={"payment": {}, "providerId": 5, "applyDateTime": "2022-05-25 01:35:24"},
    ),
]
