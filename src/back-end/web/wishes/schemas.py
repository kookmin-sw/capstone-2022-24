"""Wish API descriptions"""
from drf_spectacular.utils import OpenApiExample

WISH_LIST_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success example",
        value={
            "page": {"limit": 5, "offset": 3, "totalCount": 14},
            "results": [
                {
                    "id": 156,
                    "tmdbId": 197248,
                    "title": "살인을 말하다: 존 웨인 게이시 테이프",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/dc9IY0ZT2T3gw0RfjmQdsoWp992.jpg",
                    "dateTime": "2022-05-17T03:10:23",
                },
                {
                    "id": 34,
                    "tmdbId": 109445,
                    "title": "겨울왕국",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/nelAGS4rcZm2Qyuy3TSNWgU2mEL.jpg",
                    "dateTime": "2022-05-17T03:10:26",
                },
                {
                    "id": 130,
                    "tmdbId": 245706,
                    "title": "트루 스토리",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/8MR4VUPSd1PHYmgTy6keYBFTKme.jpg",
                    "dateTime": "2022-05-17T03:10:30",
                },
                {
                    "id": 101,
                    "tmdbId": 588228,
                    "title": "내일의 전쟁",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/34nDCQZwaEvsy4CFO5hkGRFDCVU.jpg",
                    "dateTime": "2022-05-17T03:10:34",
                },
                {
                    "id": 115,
                    "tmdbId": 10521,
                    "title": "신부들의 전쟁",
                    "posterUrl": "https://image.tmdb.org/t/p/w500/9RFu7GMsyGUffvuSUVjP5pbQWYX.jpg",
                    "dateTime": "2022-05-17T03:10:38",
                },
            ],
        },
    ),
]
