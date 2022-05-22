"""Setting Chrome driver for dynamic Crawling by Checking Os"""
import os
import platform

driver_path_dict = {
    "Windows": "\\chromewebdrive\\chromedrive_win32\\chromedriver.exe",  # Window
    "Darwin": "\\chromewebdrive\\chromedriver_mac64\\chromedriver.exe",  # Mac
    "Darwin Kernel": "\\chromewebdrive\\chromedriver_mac64\\chromedriver.exe",  # Mac
}


def setting_driver_path():
    """Method : Setting Chrome drivder path"""
    driver_path = driver_path_dict[platform.system()]
    path = os.getcwd() + driver_path
    return path
