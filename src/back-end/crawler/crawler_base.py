"""collecting frequently used method and redundantly used variables for crawling"""
import json
import os
import sys

import environ
import requests
from check_env import setting_env

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

env = environ.Env(DEBUG=(bool, False))
setting_env()
DEBUG = True

watch_providers = ["8", "337", "356", "97", "119"]
none_providers_list = ["356"]
api_key = env("MOVIE_API_KEY_V3")
language = "ko-KR"
watch_region = "KR"
MAX_PAGE_LIMIT = 500

provider_link_dict = {
    8: "https://www.netflix.com/kr/",
    356: "https://www.wavve.com/",
    97: "https://watcha.com/",
    337: "https://www.disneyplus.com/ko-kr",
    119: "https://www.primevideo.com/",
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
