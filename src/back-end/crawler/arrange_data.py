from datetime import datetime

from crawler_base import check_vaild, provider_link_dict, watch_providers


def arrange_movie_data(dicts):
    """method: Arrange base movie info in dicts to the format"""

    result = []

    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value["data"][1]
        eng_data = value["data"][3]

        try:
            date_time_str = movie_data["release_date"]
            date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d").date()
        except:
            date_time_obj = None

        poster_path = check_vaild(movie_data, "poster_path")

        if poster_path is not None:
            poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"

        title_english = eng_data["title_english"]

        object_movie = {
            "tmdb_id": tmdb_id,
            "title": movie_data["title"],
            "release_date": date_time_obj,
            "film_rating": None,
            "category": "MV",
            "poster_url": poster_url,
            "title_english": title_english,
        }
        result.append(object_movie)
        break

    return result


def arrange_movie_detail(dicts):
    """method: Arrange movie detail, genre, production_country info in dicts to the format"""

    detail_list = []
    genre_list = []
    production_country_list = []

    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value["data"][1]

        """Arrange detail data"""
        runtime = check_vaild(movie_data, "runtime")

        object_detail = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "runtime": runtime,
        }
        detail_list.append(object_detail)

        """Arrange genre data"""
        genres = []
        genre_data = check_vaild(movie_data, "genres")
        for itme in genre_data:
            genres.append(itme["name"])

        object_genre = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "genres": genres,
        }
        genre_list.append(object_genre)

        """Arrange production country data"""
        production_countries = []
        production_country_data = check_vaild(movie_data, "production_countries")

        for item in production_country_data:
            production_countries.append(item["iso_3166_1"])

        object_production_country = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "production_countries": production_countries,
        }
        production_country_list.append(object_production_country)
        break

    return detail_list, genre_list, production_country_list


def arrange_movie_provider(dicts):
    """method: Arrange movie provider info in dicts to the format"""

    provider_list = []
    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value["data"][2]["providers"]

        offer_type_list = list(movie_data.keys())
        offer_type_list.remove("link")

        providers = []
        for item in offer_type_list:
            for iter in movie_data[item]:
                if str(iter["provider_id"]) in watch_providers:
                    provider_id = iter["provider_id"]
                    provider = {
                        "offer_type": item,
                        "provider_id": provider_id,
                        "link": provider_link_dict[provider_id],
                        "deadline": None,
                    }
                    providers.append(provider)

        crawling_time_str = value["data"][0]["crawling_time"]
        crawling_time_obj = datetime.strptime(crawling_time_str, "%Y-%m-%d %H:%M:%S")

        object_providers = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "crawling_time": crawling_time_obj,
            "providers": providers,
        }
        provider_list.append(object_providers)
        break

    return provider_list


def arrange_tv_data(dicts):
    """method: Arrange base tv info in dicts to the format"""

    result = []

    for key, value in dicts.items():
        tmdb_id = key
        tv_data = value["data"][1]
        eng_data = value["data"][3]
        film_rating_data = value["data"][4]["results"]

        try:
            date_time_str = tv_data["first_air_date"]
            date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d").date()
        except:
            date_time_obj = None

        poster_path = check_vaild(tv_data, "poster_path")

        if poster_path is not None:
            poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"

        title_english = eng_data["title_english"]

        film_rating = None
        for item in film_rating_data:
            if item["iso_3166_1"] == "KR":
                film_rating = item["rating"]

        object_tv = {
            "tmdb_id": tmdb_id,
            "title": tv_data["name"],
            "release_date": date_time_obj,
            "film_rating": film_rating,
            "category": "TV",
            "poster_url": poster_url,
            "title_english": title_english,
        }
        result.append(object_tv)
        break

    return result


def arrange_tv_detail(dicts):
    """method: Arrange tv detail, genre, production_country info in dicts to the format"""

    detail_list = []
    genre_list = []
    production_country_list = []

    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value["data"][1]

        """Arrange detail data"""
        runtime = None

        object_detail = {
            "tmdb_id": tmdb_id,
            "category": "TV",
            "runtime": runtime,
        }
        detail_list.append(object_detail)

        """Arrange genre data"""
        genres = []
        genre_data = check_vaild(movie_data, "genres")
        for itme in genre_data:
            genres.append(itme["name"])

        object_genre = {
            "tmdb_id": tmdb_id,
            "category": "TV",
            "genres": genres,
        }
        genre_list.append(object_genre)

        """Arrange production country data"""
        production_countries = []
        production_country_data = check_vaild(movie_data, "production_countries")

        for item in production_country_data:
            production_countries.append(item["iso_3166_1"])

        object_production_country = {
            "tmdb_id": tmdb_id,
            "category": "TV",
            "production_countries": production_countries,
        }
        production_country_list.append(object_production_country)
        break

    return detail_list, genre_list, production_country_list


def arrange_tv_provider(dicts):
    """method: Arrange tv provider info in dicts to the format"""

    provider_list = []
    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value["data"][2]["provider"]

        crawling_time_str = value["data"][0]["crawling_time"]
        crawling_time_obj = datetime.strptime(crawling_time_str, "%Y-%m-%d %H:%M:%S")

        providers = []
        for item in movie_data:
            provider_id = int(item["provider_id"])

            provider = {
                "offer_type": item["offer_type"],
                "provider_id": provider_id,
                "link": provider_link_dict[provider_id],
                "deadline": None,
            }
            providers.append(provider)

        object_providers = {
            "tmdb_id": tmdb_id,
            "category": "TV",
            "crawling_time": crawling_time_obj,
            "providers": providers,
        }
        provider_list.append(object_providers)
        break

    return provider_list
