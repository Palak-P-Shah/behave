from common import *
# driver = webdriver.Chrome(ChromeDriverManager().install())


def load_initial_article_of_most_popular(driver):
    print("function called load_initial_article_of_most_popular")
    initial_article = driver.find_element(
        By.XPATH,
        "//div[@class='side-tabs']//ol//li[1]//a")
    actions = ActionChains(driver)
    actions.move_to_element(initial_article).perform()
    title = initial_article.get_attribute("title")
    initial_article.click()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
        By.XPATH, "html/head/title")))
    WebDriverWait(driver, 40).until(ec.title_is(title+" - SHADOW & ACT"))


def verify_injected_video(driver):
    print("function called verify_injected_video")
    # check for presence of video
    tmp_video_chk = driver.find_elements(By.XPATH, "(//div[@class='jwplayer image-wrapper image-wrapper--16x9'])[1]")
    assert len(tmp_video_chk) > 0, "within afrotech.com , injected video is not present in this article :" + driver.title
    if len(tmp_video_chk) > 0:
        print("injected video is present")
    # wait till the time main video screen is available
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((
        By.XPATH, "(//div[@class='jwplayer image-wrapper image-wrapper--16x9'])[1]")))
    # wait till the time jw player of the main video screen is available
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((
        By.XPATH, "//div[@class='jw-media jw-reset']")))
    # look for container element having video and adv
    adv_and_video_container = driver.find_element(
        By.XPATH,
        "//div[@class='jw-media jw-reset']")
    # move to the container element having video and adv
    actions = ActionChains(driver)
    actions.move_to_element(adv_and_video_container).perform()
    # wait for the video to be present
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((
        By.XPATH, "//video[@class='jw-video jw-reset']")))
    video_chk = driver.find_elements(By.XPATH, "//video[@class='jw-video jw-reset']")
    # check for the video to be present
    if len(video_chk) > 0:
        # if video is present
        print("video is present")
    else:
        print("video not present")
        video = driver.find_element(By.XPATH, "//video[@class='jw-video jw-reset']")
        assert video.is_displayed(), "Video does not Autoplay when in view"
    # move to the video
    injected_video = driver.find_element(
        By.XPATH,
        "(//div[@class='jwplayer image-wrapper image-wrapper--16x9'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(injected_video).perform()
    # wait till the time video auto plays when in view
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//video[@class='jw-video jw-reset']")))
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((
        By.XPATH, "//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")))
    within_video_adv = driver.find_elements(
        By.XPATH, "//div[@class='videoAdUiAutoClose']")
    # check till the time video auto plays when in view
    if len(within_video_adv) > 0:
        print("image Adv present in injected video")
        actions = ActionChains(driver)
        actions.move_to_element(within_video_adv[0]).perform()
        assert within_video_adv[0].is_displayed(), "Injected Video does not Autoplay when in view"


def verify_pic_in_pic_window(driver):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.PAGE_DOWN)
    print("page scrolled down once")
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((
        By.XPATH,
        "//div[@class='jw-overlays jw-reset']")))
    pic_in_pic_player_window_chk = driver.find_elements(By.XPATH, "//div[@class='jw-overlays jw-reset']")
    if len(pic_in_pic_player_window_chk) > 0:
        print("pic in pic floating window on page scroll of injected video is present")
    else:
        pic_in_pic_player_window = driver.find_element(By.XPATH, "//div[@class='jw-overlays jw-reset']")
        assert \
            pic_in_pic_player_window.is_displayed(), \
            "pic in pic jw player floating window is not present for injected video for article :" + driver.title


def verify_read_full_article(driver):
    print("function called read_full_article")
    read_full_article_btn = driver.find_element(
        By.XPATH,
        "(//button[@class='btn btn--primary bg-white'][normalize-space()='Read Full Article'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(read_full_article_btn).perform()
    read_full_article_btn.click()
    author_chk = driver.find_elements(
        By.XPATH,
        "(//div[@class='sa-article__meta sa-article__meta--bottom d-flex align-items-center font-secondary'])[1]")
    if len(author_chk) > 0:
        print("Read Full Article Button working as expected")
    else:
        author = driver.find_element(
            By.XPATH,
            "(//div[@class='sa-article__meta sa-article__meta--bottom d-flex align-items-center font-secondary'])[1]")
        assert author.is_displayed(), "On Clicking Read Full Article button, Author is not displayed for article "+driver.title

