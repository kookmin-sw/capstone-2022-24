"""dynamic crawling discontinue data for Watcha"""

import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from setting_dynamic_crawl import setting_driver_path


def infinite_loop(driver):
    """Method : Infinite scrolling for dynamic crawling"""
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height


def get_WC_discontinue_link():
    """Method: crawl Watcha upcoming release video links"""

    URL = "https://watcha.com/staffmades/3740?external_link_referer=copytopaste&ref=share"

    path = setting_driver_path()
    driver = webdriver.Chrome(path)

    driver.get(url=URL)
    time.sleep(3)

    discontinue_link_list = []
    infinite_loop(driver)

    expire_list = driver.find_elements(by=By.CLASS_NAME, value="css-1hqk0rn")
    for item in expire_list:
        title = item.find_element(by=By.CLASS_NAME, value="css-1fucs4t-StyledText.eb5y16b1").text
        image = item.find_element(
            by=By.CSS_SELECTOR,
            value="div > div.css-cssveg > div.css-omgs1s > div.css-fcehsw-StyledSelf.e1q5rx9q0 > span",
        )
        while True:
            ActionChains(driver).move_to_element(image).perform()
            time.sleep(3)
            try:
                link_image_link = item.find_element(
                    by=By.CSS_SELECTOR,
                    value="div > div.css-cssveg > div.css-18xbqro.content-preview-enter-done > div > div.css-1jy0ler.overlay-transition-enter-done > a",
                ).get_attribute("href")
                break
            except:
                pass
        video_link = link_image_link
        video = {"title": title, "link": video_link}
        discontinue_link_list.append(video)

    time.sleep(5)
    driver.close()
    return discontinue_link_list


def get_WC_discontinue_data(link_list):
    """Method: crawl Watcha upcoming release video detail info"""
    watcha_list = []
    for item in link_list:
        req = requests.get(item["link"])
        source = req.text
        soup = BeautifulSoup(source, "html.parser")

        category = soup.select_one("span.css-o7gapb").get_text()
        overview = soup.select_one("p.css-f8koiq").get_text()
        release_year = soup.select_one("span.css-4uznui").get_text()
        video_dict = {
            "title": item["title"],
            "category": category,
            "deadline": overview[1:6],
            "release_year": release_year[:4],
        }
        watcha_list.append(video_dict)

    return watcha_list


if __name__ == "__main__":
    WC_data_path = "./WachaDiscontinue.json"
    watcha_link_list = get_WC_discontinue_link()
    watcha_list = get_WC_discontinue_data(watcha_link_list)
    print(watcha_list)
    with open(WC_data_path, "w") as outfile:
        json.dump(watcha_list, outfile)
