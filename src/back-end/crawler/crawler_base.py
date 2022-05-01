import json

import environ
from crawling_movie import getMovieData
from crawling_TV import getTvData

env = environ.Env(DEBUG=(bool, False))
# environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

DEBUG = True

watch_providers = ["8", "337", "356", "97", "119"]
none_providers_list = ["356"]
api_key = env("KEY")
language = "ko-KR"
watch_region = "KR"


def checkSample(id, path):
    """method: 이미 있는 데이터를 확인하는 용도"""
    file_path = path
    with open(file_path, "r") as infile:  # open 해서 데이터 확인 할것임
        Sample_data = json.load(infile)
        Sample_data = json.dumps(Sample_data)
    if str(id) in Sample_data:  # 이미 데이터가 있음
        return True
    else:  # 데이터 없음
        return False


if __name__ == "__main__":
    Movie_data_path = "/movieSample.json"
    movie_data = getMovieData(Movie_data_path)

    Tv_data_path = "/TvSample.json"
    tv_data = getTvData(Tv_data_path)
    with open(Movie_data_path, "w") as outfile:
        json.dump(movie_data, outfile)
