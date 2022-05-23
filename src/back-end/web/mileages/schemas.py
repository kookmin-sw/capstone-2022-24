"""Example schemas in drf-spectacular"""
from drf_spectacular.utils import OpenApiExample

MILEAGES_LIST_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success Example (200 OK)",
        value=[
            {"amount": 3000, "renewalDateTime": "2022-05-22 03:38:21"},
            {"amount": -2000, "renewalDateTime": "2022-05-22 03:38:34"},
            {"amount": 1000, "renewalDateTime": "2022-05-22 03:38:52"},
            {"amount": -1000, "renewalDateTime": "2022-05-22 03:41:55"},
        ],
    )
]

MILEAGE_POST_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success Example (200 OK)",
        value={
            "amount": 5000,
            "renewalDateTime": "2022-05-22 03:51:03",
            "nowTotalMileages": 7000,
        },
    )
]

MILEAGE_PARTIAL_UPDATE_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success Example (200 OK)",
        value={"amount": -5000, "renewalDateTime": "2022-05-22 03:51:38", "nowTotalMileages": 2000},
    )
]
