from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

url_name = "http://staging.afrotech.com/"


def launch_browser_and_app(driver):
    driver.maximize_window()
    driver.get(url_name)
    time.sleep(2)
    print(driver.title)


def post_page_load_pop_up(driver):
    try:
        footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
        driver.execute_script("arguments[0].click();", footer_xpath)
        assert driver.title == "AfroTech", "title does not match"
    except NoSuchElementException:
        print("cookies pop-up does not exist")
