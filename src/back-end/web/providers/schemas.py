"""Example schemas in providers application"""
from drf_spectacular.utils import OpenApiExample

PROVIDER_LIST_EXAMPLES = [
    OpenApiExample(
        "Success example (200)",
        response_only=True,
        value={
            "appliedProviders": [
                {
                    "id": 5,
                    "name": "AP",
                    "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                    "link": "https://www.primevideo.com/ref=atv_nb_logo?_encoding=UTF8&language=ko_KR",
                },
                {
                    "id": 6,
                    "name": "LF",
                    "logoUrl": "https://blog.kakaocdn.net/dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png",
                    "link": "https://laftel.net/",
                },
            ],
            "notAppliedProviders": [],
        },
    )
]
