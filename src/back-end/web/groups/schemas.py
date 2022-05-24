"""example schemas of spectacular docs"""
from drf_spectacular.utils import OpenApiExample

GROUP_DETAIL_SERIALIZER_EXAMPLES = [
    OpenApiExample(
        name="Success example (200, Recruiting)",
        response_only=True,
        value=(
            {
                "id": 1,
                "provider": {
                    "id": 5,
                    "tmdbId": 119,
                    "name": "아마존 프라임",
                    "link": "https://www.primevideo.com/offers/nonprimehomepage/ref=atv_nb_lcl_ko_KR",
                    "logoUrl": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
                },
                "status": "Recruiting",
                "account": {
                    "id": 1,
                    "identifier": None,
                    "password": None,
                    "creationDateTime": None,
                    "lastModificationDateTime": None,
                },
                "timeStamps": {
                    "creationDateTime": "2022-05-20 02:33:15",
                    "startWatchingDateTime": None,
                    "endWatchingDateTime": None,
                    "endReportingDateTime": None,
                },
                "fellows": [],
                "report": {"reported": False, "reportCount": 0, "leaderReportCount": 0},
                "role": None,
            }
        ),
    )
]
