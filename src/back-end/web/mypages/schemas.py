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
                },
                "groups": {
                    "default": {
                        "fellows": [],
                        "provider": {
                            "id": 5,
                            "tmdbId": 119,
                            "name": "AP",
                            "link": "",
                            "logoUrl": "https://some.storage.com/providers/logo_images/app/back-end/static/"
                            "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                        },
                        "applyDateTime": "2022-05-14T04:38:35",
                        "status": "Recruiting",
                    },
                    "others": [
                        {
                            "id": 1,
                            "provider": {
                                "id": 1,
                                "tmdbId": 8,
                                "name": "NF",
                                "link": "",
                                "logoUrl": "https://some.storage.com/providers/logo_images/app/back-end/static/"
                                "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                            },
                            "status": "Recruited",
                        }
                    ],
                },
                "videos": {
                    "recentViews": [],
                    "watchMarks": [],
                    "wishes": [
                        {
                            "id": 40,
                            "tmdbId": 19995,
                            "posterUrl": "https://image.tmdb.org/t/p/original/zygmx5abXeDpr3fWYX4jlXFZ1wh.jpg",
                        }
                    ],
                    "stars": [],
                },
            }
        ],
    ),
    OpenApiExample(
        response_only=True,
        name="Success Example",
        value={
            "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
            ".eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMjE3Mjg0LCJpYXQiOjE2NTIyMTAwODQsImp0aSI6IjA0ODY3"
            "NjA2NTIzMzRmMDhiN2Q3MTc2NjQ0NTg3YjI3IiwidXNlcl9pZCI6Mjl9.CDOzt"
            "k-o6jvEbfdzAouTAgIypzFgAcm4jbRzzGeDais",
            "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
            ".eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjIzMTY4NCwiaW"
            "F0IjoxNjUyMjEwMDg0LCJqdGkiOiIwNjUxZjdlNGJlMDY0ZjEzYWY5MjU2ZGIyN"
            "GVlNTVkNiIsInVzZXJfaWQiOjI5fQ.ael6_7GMvE39X6qESW__gikrLrbQAeYTtAllWmN_sYc",
            "user": {
                "nickname": "Ongot",
                "name": "ongot",
                "email": "ongot@123.com",
                "cellPhoneNumber": "010-1111-1111",
                "profileImageUrl": "https://upload.wikimedia.org/wikipedia/"
                "commons/thumb/a/ab/Swagger-logo.png/150px-Swagger"
                "-logo.png",
                "birthday": "1998-01-01",
                "isActive": True,
                "isVerified": True,
            },
        },
    ),
]
