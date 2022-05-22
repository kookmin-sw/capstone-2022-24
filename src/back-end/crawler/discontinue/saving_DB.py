"""Save the data in the actual DB"""

import json
import os
import sys
from datetime import datetime

import environ
import MySQLdb

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from check_env import setting_env

"""==========Model for Saving data==========="""


def saving_NF_data(NF_list):
    """Method: Save the NF data in Video Provider model"""
    for item in NF_list:
        if item["category"] == "series":
            category = "TV"
        else:
            category = "MV"

        sql_id = (
            "SELECT id FROM videos WHERE title_english =%s AND category= %s AND DATE(release_date) BETWEEN %s AND %s"
        )
        values = (
            item["title"],
            category,
            item["release_year"] + "-01-01",
            item["release_year"] + "-12-31",
        )
        cursor.execute(sql_id, values)

        try:
            video_id = cursor.fetchall()[0][0]
        except:
            continue

        sql_provider = "SELECT id FROM provider WHERE name = 'NF'"
        cursor.execute(sql_provider)
        provider_id = cursor.fetchall()[0][0]

        date_time_obj = datetime.strptime(item["discontinue_date"], "%Y-%m-%d").date()
        sql = "UPDATE video_providers SET deadline = %s WHERE video_id= %s AND provider_id= %s"
        values = (
            date_time_obj,
            video_id,
            provider_id,
        )
        cursor.execute(sql, values)
        conn.commit()


def saving_WC_data(NF_list):
    for item in NF_list:

        if "에피소드" in item["category"]:
            category = "TV"
        else:
            category = "MV"

        sql_id = "SELECT id FROM videos WHERE title =%s AND category= %s AND DATE(release_date) BETWEEN %s AND %s"
        values = (
            item["title"],
            category,
            item["release_year"] + "-01-01",
            item["release_year"] + "-12-31",
        )
        cursor.execute(sql_id, values)

        try:
            video_id = cursor.fetchall()[0][0]
        except:
            continue

        sql_provider = "SELECT id FROM provider WHERE name = 'WC'"
        cursor.execute(sql_provider)
        provider_id = cursor.fetchall()[0][0]

        discontinue_date = str(datetime.today().year) + "/" + item["deadline"].rstrip()
        date_time_obj = datetime.strptime(discontinue_date, "%Y/%m/%d").date()
        sql = "UPDATE video_providers SET deadline = %s WHERE video_id= %s AND provider_id= %s"
        values = (
            date_time_obj,
            video_id,
            provider_id,
        )
        cursor.execute(sql, values)
        conn.commit()


if __name__ == "__main__":

    """==========environment value setiing==========="""

    env = environ.Env(DEBUG=(bool, False))
    setting_env()
    DEBUG = True

    """==========DB Connect==========="""

    conn = MySQLdb.connect(
        user=env("DB_USER"),
        passwd=env("DB_PASSWORD"),
        host=env("DB_HOST"),
        port=int(env("DB_PORT")),
        db=env("DB_NAME"),
    )
    cursor = conn.cursor()

    """==========Neflix data Saving==========="""
    file_NF_path = "./NeflixDiscontinue.json"

    with open(file_NF_path, "r", encoding="utf8") as file:
        contents = file.read()
        Netfilx_dict = json.loads(contents)

    saving_NF_data(Netfilx_dict)

    """==========Watcha data Saving==========="""
    file_WC_path = "./WatchaDiscontinue.json"

    with open(file_WC_path, "r", encoding="utf8") as file:
        contents = file.read()
        Watcha_dict = json.loads(contents)

    saving_WC_data(Watcha_dict)
