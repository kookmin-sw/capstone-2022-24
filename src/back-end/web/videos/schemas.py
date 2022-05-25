"""Video View API descriptions"""
from drf_spectacular.utils import OpenApiExample

DETAIL_MOVIE_VIEW_EXAPLE = [
    OpenApiExample(
        response_only=True,
        name="Success Example",
        value={
            "videoId": 60,
            "posterUrl": "https://image.tmdb.org/t/p/w500/2R8smeSDkPx6TKIRveKPXi0JVI6.jpg",
            "title": "언차티드",
            "releaseYear": "2022",
            "releaseDate": "02-10",
            "titleEnglish": "Uncharted",
            "overview": (
                "평범한 삶을 살던 네이선은 인생을 바꿀 뜻밖의 제안을 받는다. 그의 미션은 크루와 함께 사라진 형과 500년 전 잃어버린 천문학적인 가치를"
                " 지닌 트레져를 찾아내는 것. 그러나 몬카다의 위협 속, 누구보다 빠르게 미지의 세계에 닿기 위해 결단을 내려야만 하는데…"
            ),
            "providers": [
                {
                    "name": "WV",
                    "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                    "link": "https://www.wavve.com/",
                }
            ],
            "genres": ["액션", "모험"],
            "productionCountries": ["미국"],
            "public": {"wishCount": 0, "watchingCount": 1},
            "personal": {"wished": False, "watched": True},
            "similars": [
                {"posterUrl": "https://image.tmdb.org/t/p/w500/SkNd3gVm26389N5jPaCM5hpekh.jpg", "title": "몬테 크리스토"},
                {"posterUrl": "https://image.tmdb.org/t/p/w500/mtmb7GMXXQOpMH9Bkgka4xy18lu.jpg", "title": "스트리트 파이터"},
                {
                    "posterUrl": "https://image.tmdb.org/t/p/w500/w1SlfdoU144Sl4c8rXG9kw5jiuq.jpg",
                    "title": "포켓몬스터 극장판 - 뮤츠의 역습",
                },
                {
                    "posterUrl": "https://image.tmdb.org/t/p/w500/p2Hkd6iJ3Hu3MJbzHkyzd40zBSy.jpg",
                    "title": "ソニック★ザ★ヘッジホッグ",
                },
                {"posterUrl": "https://image.tmdb.org/t/p/w500/o6Wf8lj8P9enQQbj4pC8jVDJHxI.jpg", "title": "어둠 속에 나홀로"},
                {
                    "posterUrl": "https://image.tmdb.org/t/p/w500/a4sHmafOKKOTo2TZYtvy9CufVTz.jpg",
                    "title": "포켓몬스터 극장판 - 루기아의 탄생",
                },
            ],
        },
    )
]

DETAIL_TV_VIEW_EXAMPLE = (
    [
        OpenApiExample(
            response_only=True,
            name="Success Example",
            value={
                "videoId": 200,
                "posterUrl": "https://image.tmdb.org/t/p/w500/ekp9PbSODHiTXXqnHJ4Sq6YHkhq.jpg",
                "title": "블리치",
                "titleEnglish": "Bleach",
                "releaseYear": "2004",
                "releaseDate": "10-05",
                "filmRating": None,
                "overview": "",
                "providers": [
                    {
                        "name": "WV",
                        "logoUrl": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
                        "link": "https://www.wavve.com/",
                    }
                ],
                "genres": ["Action & Adventure", "애니메이션", "Sci-Fi & Fantasy"],
                "productionCountries": ["일본"],
                "totalSeasons": 1,
                "totalEpisodes": 366,
                "seasons": [{"number": 0, "name": "스페셜"}, {"number": 1, "name": "시즌 1"}],
                "public": {"wishCount": 1, "watchingCount": 5},
                "personal": {"wished": True, "watched": True},
                "similars": [
                    {"posterUrl": "https://image.tmdb.org/t/p/w500/97vxf06BrfiSuZJ5a03RuOHNyP0.jpg", "title": "진격의 거인"},
                    {
                        "posterUrl": "https://image.tmdb.org/t/p/w500/pOjDuclpsWGV13Nj7XtZukuZj6f.jpg",
                        "title": "소녀혁명 우테나",
                    },
                    {
                        "posterUrl": "https://image.tmdb.org/t/p/w500/9A7q9QjLoTfYLn7zejj7uRYA3IZ.jpg",
                        "title": "오란고교 사교클럽",
                    },
                    {
                        "posterUrl": "https://image.tmdb.org/t/p/w500/ej3tcxv2YYVWy6WoOeWZTcrkiI8.jpg",
                        "title": "시리얼 익스페러먼츠 레인",
                    },
                    {
                        "posterUrl": "https://image.tmdb.org/t/p/w500/wXaWK1dtA5EACL3ASDKGKBJePsS.jpg",
                        "title": "에르고 프록시",
                    },
                    {
                        "posterUrl": "https://image.tmdb.org/t/p/w500/fbdM3vtY29PkipKrBb6NuTw7VDt.jpg",
                        "title": "교향시편 유레카 세븐",
                    },
                ],
            },
        )
    ],
)
