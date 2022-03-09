
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


def navigate_to_google_page(driver):
    driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(2)
    print(driver.title)


def navigate_to_google_page_on_mobile(driver):
    driver.get("https://google.com")
    time.sleep(2)
    print(driver.title)


def search_keyword(driver, website_name):
    print("function called search_keyword")
    search_text_box = driver.find_element(By.XPATH, "//input[@title='Search']")
    search_text_box.send_keys(website_name)
    search_text_box.send_keys(Keys.RETURN)
    time.sleep(2)


def launch_app(driver):
    print("function called launch_app")
    result = driver.find_element(By.XPATH, "//a[@href='https://shadowandact.com/']")
    result.click()
    time.sleep(5)




def verify_footer_presence(driver):
    time.sleep(3)
    footer_sanda_page = driver.find_element(
      By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    assert footer_sanda_page.is_displayed(), "Footer section for SHADOWANDACT is not displayed"
    actions = ActionChains(driver)
    actions.move_to_element(footer_sanda_page).perform()
    if footer_sanda_page.is_displayed():
        print("footer section is displayed on shadowandact page")
