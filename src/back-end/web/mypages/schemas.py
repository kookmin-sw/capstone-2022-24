"""Schemas visible in drf-spectacular"""
from drf_spectacular.utils import OpenApiExample

MYPAGE_DETAIL_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success Example (Recruiting default)",
        value=[
            {
                "profile": {
                    "nickname": "ongot",
                    "name": "ongot",
                    "email": "ongot@123.com",
                    "cellPhoneNumber": "010-1234-5678",
                    "profileImageUrl": None,
                    "birthday": "1990-01-01",
                    "isActive": True,
                    "isVerified": True,
                    "totalMileage": 3200,
                },
                "groups": {
                    "default": {
                        "fellows": [],
                        "provider": {
                            "id": 6,
                            "tmdbId": 0,
                            "name": "LF",
                            "link": "https://laftel.net/",
                            "logoUrl": "https://blog.kakaocdn.net/"
                            "dn/beMRoh/btqJUNc2uBT/gLb6LDCKEemdV8IEki0St0/img.png ",
                        },
                        "applyDateTime": "2022-05-17T01:23:19",
                        "status": "Recruiting",
                    },
                    "others": [
                        {
                            "fellows": [],
                            "provider": {
                                "id": 5,
                                "tmdbId": 119,
                                "name": "AP",
                                "link": "https://default_ott_link.com",
                                "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                            },
                            "applyDateTime": "2022-05-17T01:22:47",
                            "status": "Recruiting",
                        },
                        {
                            "fellows": [],
                            "provider": {
                                "id": 4,
                                "tmdbId": 337,
                                "name": "DP",
                                "link": "https://default_ott_link.com",
                                "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                            },
                            "applyDateTime": "2022-05-17T01:23:47",
                            "status": "Recruiting",
                        },
                        {
                            "id": 1,
                            "provider": {
                                "id": 3,
                                "tmdbId": 97,
                                "name": "WC",
                                "link": "https://default_ott_link.com",
                                "logoUrl": "https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg",
                            },
                            "status": "Recruited",
                        },
                    ],
                },
                "videos": {
                    "recentViews": {
                        "page": {"limit": 3, "offset": 0, "totalCount": 4},
                        "results": [
                            {
                                "id": 9,
                                "tmdbId": 454626,
                                "posterUrl": "https://image.tmdb.org/t/p/original/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg",
                            },
                            {
                                "id": 14,
                                "tmdbId": 783461,
                                "posterUrl": "https://image.tmdb.org/t/p/original/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg",
                            },
                            {
                                "id": 19,
                                "tmdbId": 800407,
                                "posterUrl": "https://image.tmdb.org/t/p/original/hmqocSNKCgMY5yrVOOmfCUHdXkl.jpg",
                            },
                        ],
                    },
                    "watchMarks": {"page": {"limit": 3, "offset": 0, "totalCount": 0}, "results": []},
                    "wishes": {
                        "page": {"limit": 3, "offset": 0, "totalCount": 1},
                        "results": [
                            {
                                "id": 167,
                                "tmdbId": 76479,
                                "posterUrl": "https://image.tmdb.org/t/p/original/dzOxNbbz1liFzHU1IPvdgUR647b.jpg",
                            }
                        ],
                    },
                    "stars": {"page": {"limit": 3, "offset": 0, "totalCount": 0}, "results": []},
                },
            }
        ],
    ),
    OpenApiExample(
        response_only=True,
        name="Success Example",
        value={
            "profile": {
                "nickname": "ongot",
                "name": "ongot",
                "email": "ongot@123.com",
                "cellPhoneNumber": "010-1234-5678",
                "profileImageUrl": None,
                "birthday": "1990-01-01",
                "isActive": True,
                "isVerified": True,
            },
            "groups": {
                "default": {
                    "provider": {
                        "id": 3,
                        "tmdbId": 356,
                        "name": "WC",
                        "link": "",
                        "logoUrl": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
                    },
                    "status": "Recruiting",
                    "timeStamps": {
                        "creationDateTime": "2022-05-16T20:14:17",
                        "startWatchingDateTime": "2022-05-16T20:14:31",
                        "endWatchingDateTime": None,
                        "endReportingDateTime": "2022-05-19T20:14:31",
                    },
                    "fellows": [
                        {"id": 1, "nickname": "ongot", "profileImageUrl": None, "isLeader": True, "isMyself": True},
                        {
                            "id": 2,
                            "nickname": "캡스톤",
                            "profileImageUrl": "https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop"
                            "3.daumcdn.net%2Fshophow%2Fp%2FS16182251276.jpg%3Fut%3D20220129023802",
                            "isLeader": True,
                            "isMyself": False,
                        },
                    ],
                    "account": {
                        "id": 1,
                        "identifier": None,
                        "password": None,
                        "creationDateTime": None,
                        "lastModificationDateTime": None,
                    },
                    "report": {"reported": False, "reportCount": 0, "leaderReportCount": 0},
                },
                "others": [],
            },
            "videos": {
                "recentViews": {
                    "page": {"limit": 5, "offset": 0, "totalCount": 4},
                    "results": [
                        {
                            "id": 9,
                            "tmdbId": 454626,
                            "posterUrl": "https://image.tmdb.org/t/p/original/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg",
                        },
                        {
                            "id": 14,
                            "tmdbId": 783461,
                            "posterUrl": "https://image.tmdb.org/t/p/original/ppn4ZO8qmylxRwFjfBWPkmMRdSs.jpg",
                        },
                        {
                            "id": 19,
                            "tmdbId": 800407,
                            "posterUrl": "https://image.tmdb.org/t/p/original/hmqocSNKCgMY5yrVOOmfCUHdXkl.jpg",
                        },
                        {
                            "id": 38,
                            "tmdbId": 166426,
                            "posterUrl": "https://image.tmdb.org/t/p/original/arcIFL50IPQT7JDG2SD6tzcOlRL.jpg",
                        },
                    ],
                },
                "watchMarks": {"page": {"limit": 5, "offset": 0, "totalCount": 0}, "results": []},
                "wishes": {
                    "page": {"limit": 5, "offset": 0, "totalCount": 1},
                    "results": [
                        {
                            "id": 167,
                            "tmdbId": 76479,
                            "posterUrl": "https://image.tmdb.org/t/p/original/dzOxNbbz1liFzHU1IPvdgUR647b.jpg",
                        }
                    ],
                },
                "stars": {"page": {"limit": 5, "offset": 0, "totalCount": 0}, "results": []},
            },
        },
    ),
]
