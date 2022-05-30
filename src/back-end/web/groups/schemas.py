"""example schemas of spectacular docs"""
from drf_spectacular.utils import OpenApiExample

GROUP_DETAIL_SERIALIZER_EXAMPLES = [
    OpenApiExample(
        name="Success example (200, Recruiting)",
        response_only=True,
        value=(
            {
                "provider": {
                    "id": 5,
                    "tmdbId": 119,
                    "name": "아마존 프라임",
                    "link": "https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_ko_KR",
                    "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                },
                "status": "Recruiting",
                "timeStamps": {"applyDateTime": "2022-05-31 03:43:11"},
                "fellows": [],
                "role": "leader",
            }
        ),
    ),
    OpenApiExample(
        name="Success Example (200, Recruited)",
        response_only=True,
        value=(
            {
                "id": 2,
                "provider": {
                    "id": 6,
                    "tmdbId": 0,
                    "name": "라프텔",
                    "link": "https://laftel.net/",
                    "logoUrl": "https://blog.kakaocdn.net/dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png",
                },
                "status": "Recruited",
                "account": {
                    "id": 2,
                    "identifier": None,
                    "password": None,
                    "creationDateTime": None,
                    "lastModificationDateTime": None,
                },
                "timeStamps": {
                    "creationDateTime": "2022-05-20 02:33:25",
                    "startWatchingDateTime": None,
                    "endWatchingDateTime": None,
                    "endReportingDateTime": None,
                },
                "fellows": [
                    {"id": 4, "nickname": "string", "profileImageUrl": None, "isLeader": False, "isMyself": False},
                    {
                        "id": 2,
                        "nickname": "캡스톤",
                        "profileImageUrl": "https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3."
                        "daumcdn.net%2Fshophow%2Fp%2FS16182251276.jpg%3Fut%3D20220129023802",
                        "isLeader": False,
                        "isMyself": False,
                    },
                    {"id": 1, "nickname": "ongot", "profileImageUrl": None, "isLeader": True, "isMyself": True},
                ],
                "report": {"reported": False, "reportCount": 0, "leaderReportCount": 0},
            }
        ),
    ),
]


GROUP_PAYMENT_EXAMPLES = [
    OpenApiExample(
        name="Success Example (201)",
        response_only=True,
        value={
            "paymentId": 12,
            "amount": 4500,
            "requestDateTime": "2022-05-24 12:34:56",
        },
    )
]
