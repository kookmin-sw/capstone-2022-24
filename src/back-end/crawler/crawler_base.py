"""collecting frequently used method and redundantly used variables for crawling"""
import json
import os
import sys

import environ
import requests

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from web.config.settings.base import ENV_DIR

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

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


def is_Korean_included(word):
    """Method: Checking if title is not included Korean"""
    for i in word:
        if ord(i) > int("0x1100", 16) and ord(i) < int("0x11ff", 16):
            return True
        if ord(i) > int("0x3131", 16) and ord(i) < int("0x318e", 16):
            return True
        if ord(i) > int("0xa960", 16) and ord(i) < int("0xa97c", 16):
            return True
        if ord(i) > int("0xac00", 16) and ord(i) < int("0xd7a3", 16):
            return True
        if ord(i) > int("0xd7b0", 16) and ord(i) < int("0xd7fb", 16):
            return True
    return False
