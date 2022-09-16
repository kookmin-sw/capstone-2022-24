"""Spectacular example schemas in notification application"""

from drf_spectacular.utils import OpenApiExample

NOTIFICATION_LIST_EXAMPLES = [
    OpenApiExample(
        response_only=True,
        name="Success Example(limit=3, offset=1, read=Y)",
        value={
            "page": {"limit": 3, "offset": 1, "totalCount": 2},
            "results": [
                {
                    "id": 4,
                    "provider": {
                        "id": 5,
                        "name": "아마존 프라임",
                        "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                    },
                    "content": {"category": "계정", "keyword": "정보 변경", "message": "모임 계정 정보가 변경되었습니다!"},
                    "hasRead": True,
                    "creationDateTime": "2022-04-27 04:40:43",
                    "deadlineDateTime": None,
                }
            ],
        },
    )
]
