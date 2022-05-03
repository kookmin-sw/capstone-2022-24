"""collecting frequently used method and redundantly used variables for crawling
"""
import json

import environ
import requests

env = environ.Env(DEBUG=(bool, False))
# environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

DEBUG = True

watch_providers = ["8", "337", "356", "97", "119"]
none_providers_list = ["356"]
api_key = ""
# api_key = env("KEY")
language = "ko-KR"
watch_region = "KR"

provider_link_dict = {
    "8": "https://www.netflix.com/kr/",
    "356": "https://www.wavve.com/",
    "97": "https://watcha.com/",
    "337": "https://www.disneyplus.com/ko-kr",
    "119": "https://www.primevideo.com/",
}


def check_vaild(dict, string):
    """Method: checking if the value exists in the dict"""
    try:
        obj = dict[string]
    except:
        obj = None
    return obj


def get_request_to_object(url):
    """Method: Receiving json data through URL and deserialize it into a python object"""
    response = requests.get(url)
    contents = response.text

    json_ob = json.loads(contents)
    return json_ob


def check_sample(id, path):
    """Method: Checking if data already exists"""
    file_path = path
    try:
        with open(file_path, "r") as infile:
            Sample_data = json.load(infile)
            Sample_data = json.dumps(Sample_data)
    except:
        return False

    if str(id) in Sample_data:
        return True
    else:
        return False


if __name__ == "__main__":
    """
    movie_data_path = "/movieSample.json"
    movie_data = get_movie_data(movie_data_path)
    with open(movie_data_path, "w") as outfile:
        json.dump(movie_data, outfile)

    tv_data_path = "/TvSample.json"
    tv_data = get_tv_data(tv_data_path)
    with open(tv_data_path, "w") as outfile:
        json.dump(tv_data, outfile)
    """
