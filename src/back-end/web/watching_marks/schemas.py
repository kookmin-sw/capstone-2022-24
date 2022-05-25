"""Wish API descriptions"""
from drf_spectacular.utils import OpenApiExample

WATCHINGMARK_LIST_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success example",
        value={
            "page": {"limit": 5, "offset": 0, "totalCount": 2},
            "results": [
                {
                    "id": 15,
                    "category": "MV",
                    "title": "샹치와 텐 링즈의 전설",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/14L4NGrqO4r7gJtVRiSRP5rNsL5.jpg",
                    "date": "2022-05-25",
                    "time": "11:50:30",
                },
                {
                    "id": 200,
                    "category": "TV",
                    "title": "블리치",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/ekp9PbSODHiTXXqnHJ4Sq6YHkhq.jpg",
                    "date": "2022-05-25",
                    "time": "11:44:54",
                },
            ],
        },
    ),
]
