"""example schemas of spectacular docs"""
from drf_spectacular.utils import OpenApiExample

GROUP_DETAIL_SERIALIZER_EXAMPLES = [
    OpenApiExample(
        name="Success example (200)",
        response_only=True,
        value=(
            {
                "id": 1,
                "provider": {
                    "id": 4,
                    "tmdbId": 337,
                    "name": "DP",
                    "link": "https://default_ott_link.com",
                    "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                },
                "status": "Recruiting",
                "account": {
                    "id": 1,
                    "identifier": None,
                    "password": None,
                    "creationDateTime": None,
                    "lastModificationDateTime": None,
                },
                "fellows": {
                    "fellows": [
                        {"id": 1, "nickname": "ongot", "profileImageUrl": None, "isLeader": False, "isMyself": False},
                        {
                            "id": 2,
                            "nickname": "캡스톤",
                            "profileImageUrl": "https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3."
                            "daumcdn.net%2Fshophow%2Fp%2FS16182251276.jpg%3Fut%3D20220129023802",
                            "isLeader": True,
                            "isMyself": False,
                        },
                    ],
                    "report": {"reported": False, "reportCount": 0, "leaderReportCount": 0},
                },
                "report": {
                    "fellows": [
                        {"id": 1, "nickname": "ongot", "profileImageUrl": None, "isLeader": False, "isMyself": False},
                        {
                            "id": 2,
                            "nickname": "캡스톤",
                            "profileImageUrl": "https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.da"
                            "umcdn.net%2Fshophow%2Fp%2FS16182251276.jpg%3Fut%3D20220129023802",
                            "isLeader": True,
                            "isMyself": False,
                        },
                    ],
                    "report": {"reported": False, "reportCount": 0, "leaderReportCount": 0},
                },
                "timeStamps": {
                    "creationDateTime": "2022-05-20T07:20:29",
                    "startWatchingDateTime": None,
                    "endWatchingDateTime": None,
                    "endReportingDateTime": None,
                },
            }
        ),
    )
]
