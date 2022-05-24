"""Swagger schema examples"""
from drf_spectacular.utils import OpenApiExample

GROUP_APPLY_EXAMPLES = [
    OpenApiExample(
        name="Success example (200)",
        response_only=True,
        value={"payment": {}, "providerId": 5, "applyDateTime": "2022-05-25 01:35:24"},
    ),
    OpenApiExample(
        name="Request Example",
        request_only=True,
        value={
            "providerId": 5,
        },
    ),
]
