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
                    "name": "아마존 프라임",
                    "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                    "link": "https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_ko_KR",
                    "charge": {
                        "subscriptionType": {"name": "프라임 요금제", "duration": "30 00:00:00", "detail": "국내에서만 이용 가능"},
                        "numberOfSubscribers": 3,
                        "serviceChargePerMember": 4500,
                        "subscriptionChargePerMember": 3000,
                        "totalSubscriptionCharge": 6000,
                    },
                },
                {
                    "id": 6,
                    "name": "라프텔",
                    "logoUrl": "https://blog.kakaocdn.net/dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png",
                    "link": "https://laftel.net/",
                    "charge": {
                        "subscriptionType": {
                            "name": "프리미엄 요금제",
                            "duration": "30 00:00:00",
                            "detail": "광고 X / 프로필 4인 / 동시재생 4인 / 최신화 시청 / 다운로드 지원 / FHD 화질 / TV 앱 지원",
                        },
                        "numberOfSubscribers": 4,
                        "serviceChargePerMember": 5500,
                        "subscriptionChargePerMember": 4000,
                        "totalSubscriptionCharge": 16000,
                    },
                },
            ],
            "notAppliedProviders": [],
            "notSupportedProviders": [
                {
                    "id": 1,
                    "name": "넷플릭스",
                    "logoUrl": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                    "link": "https://www.netflix.com/kr/",
                    "charge": None,
                },
                {
                    "id": 2,
                    "name": "웨이브",
                    "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                    "link": "https://www.wavve.com/",
                    "charge": None,
                },
                {
                    "id": 3,
                    "name": "왓챠",
                    "logoUrl": "https://oopy.lazyrockets.com/api/rest/cdn/image/"
                    "99453fde-4624-457f-8471-2393b96ccdbb.jpeg",
                    "link": "https://watcha.com/",
                    "charge": None,
                },
                {
                    "id": 4,
                    "name": "디즈니 플러스",
                    "logoUrl": "https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg",
                    "link": "https://www.disneyplus.com/ko-kr",
                    "charge": None,
                },
            ],
        },
    )
]
