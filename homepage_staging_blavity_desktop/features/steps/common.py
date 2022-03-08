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

url_name = "http://staging.blavity.com/"


def launch_browser_and_app(driver):
    driver.maximize_window()
    driver.get(url_name)
    time.sleep(2)
    print(driver.title)


def post_page_load_pop_up(driver):
    try:
        event_promo_pop_up = driver.find_element_by_xpath(
          "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
        driver.execute_script("arguments[0].click();", event_promo_pop_up)
    except NoSuchElementException:
        print("event promo pop-up does not exist")
    # try:
    #     driver.switch_to.frame("sp_message_iframe_565136")
    #     pop_up_text = driver.find_element(By.XPATH, "//p[normalize-space()='We value your privacy']")
    #     if pop_up_text.is_displayed():
    #         accept_button = driver.find_element(By.XPATH, "//button[@title='Accept']")
    #         accept_button.click()
    #     driver.switch_to.parent_frame()
    # except NoSuchElementException:
    #     print("blavity news privacy pop-up does not exist")
    footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
    driver.execute_script("arguments[0].click();", footer_xpath)
    assert driver.title == "The Community for Black Creativity and News - Blavity News", "title does not match"
