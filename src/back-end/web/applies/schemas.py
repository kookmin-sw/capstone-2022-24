"""Swagger schema examples"""
from drf_spectacular.utils import OpenApiExample

GROUP_APPLY_POST_EXAMPLE = [
    OpenApiExample(
        name="Success example (201)",
        response_only=True,
        value={"payment": {}, "providerId": 5, "applyDateTime": "2022-05-25 01:35:24"},
    ),
]


GROUP_APPLY_CANCEL_MEMBER_EXAMPLE = [
    OpenApiExample(
        name="Success Example (200)",
        response_only=True,
        value={"amount": 4500, "renewalDateTime": "2022-05-31 06:59:18", "nowTotalMileages": 20000},
    )
]
