"""Example schemas in providers application"""
from drf_spectacular.utils import OpenApiExample

PROVIDER_LIST_EXAMPLES = [
    OpenApiExample(
        "Success example (200)",
        response_only=True,
        value={
            "appliedProviders": [
                {
                    "id": 6,
                    "name": "라프텔",
                    "logoUrl": "https://blog.kakaocdn.net/dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png",
                    "link": "https://laftel.net/",
                }
            ],
            "notAppliedProviders": [
                {
                    "id": 5,
                    "name": "아마존 프라임",
                    "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                    "link": "https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_ko_KR",
                }
            ],
            "notSupportedProviders": [
                {
                    "id": 1,
                    "name": "넷플릭스",
                    "logoUrl": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                    "link": "https://www.netflix.com/kr/",
                },
                {
                    "id": 2,
                    "name": "웨이브",
                    "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                    "link": "https://www.wavve.com/",
                },
                {
                    "id": 3,
                    "name": "왓챠",
                    "logoUrl": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
                    "link": "https://watcha.com/",
                },
                {
                    "id": 4,
                    "name": "디즈니 플러스",
                    "logoUrl": "https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg",
                    "link": "https://www.disneyplus.com/ko-kr",
                },
            ],
        },
    )
]
