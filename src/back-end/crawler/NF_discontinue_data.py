"""crawling discontinue data for Netflix"""

import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_NF_discontine_data():
    """Method : crawl Netflix upcoming releases through the unogs site."""

    URL = "https://unogs.com/countrydetail"

    driver_path = "\\chromewebdrive\\chromedrive_win32\\chromedriver.exe"
    path = os.getcwd() + driver_path
    driver = webdriver.Chrome(path)

    driver.get(url=URL)
    time.sleep(3)
    expire_box = driver.find_element(
        by=By.CSS_SELECTOR,
        value="body > div:nth-child(15) > div:nth-child(30) > div > div.buttoncs > button:nth-child(2)",
    )
    expire_box.click()
    time.sleep(3)
    expire_list = driver.find_elements(by=By.CLASS_NAME, value="videodiv.img-rounded")
    netflix_list = []
    for item in expire_list:
        item_title = item.find_element(by=By.CSS_SELECTOR, value="div:nth-child(4) > b > span").text
        itme_category = item.find_element(by=By.CSS_SELECTOR, value="div:nth-child(4) > span:nth-child(2)").text
        itme_year = item.find_element(by=By.CSS_SELECTOR, value="div:nth-child(4) > span:nth-child(3)").text
        item_date = item.find_element(by=By.XPATH, value="b/span").text

        video_dict = {
            "title": item_title,
            "category": itme_category,
            "release_year": itme_year,
            "discontinue_date": item_date[11:],
        }
        netflix_list.append(video_dict)

    time.sleep(5)
    driver.close()

    return netflix_list


if __name__ == "__main__":
    NF_data_path = "./NeflixDiscontinue.json"
    netflix_list = get_NF_discontine_data()
    print(netflix_list)
    with open(NF_data_path, "w") as outfile:
        json.dump(netflix_list, outfile)
