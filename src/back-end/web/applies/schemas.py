"""Swagger schema examples"""
from drf_spectacular.utils import OpenApiExample

GROUP_APPLY_POST_EXAMPLES = [
    OpenApiExample(
        name="Success example (201)",
        response_only=True,
        status_codes=["POST"],
        value={"payment": {}, "providerId": 5, "applyDateTime": "2022-05-25 01:35:24"},
    ),
]

GROUP_APPLY_PUT_EXAMPLES = [
    OpenApiExample(
        name="Success example (201)",
        response_only=True,
        status_codes=["POST"],
        value={"payment": {}, "providerId": 5, "applyDateTime": "2022-05-25 01:35:24"},
    ),
]

GROUP_APPLY_REQUEST_EXAMPLES = [
    OpenApiExample(
        name="Request Example",
        request_only=True,
        value={
            "providerId": 5,
        },
    ),
]
