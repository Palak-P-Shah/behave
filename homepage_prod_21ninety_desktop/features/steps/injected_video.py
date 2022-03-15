from common import *
# driver = webdriver.Chrome(ChromeDriverManager().install())


def expand_shadow_element(element, driver):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


def load_article_mobile(driver):
    print("function called load_article_mobile")
    initial_article = driver.find_element(
        By.XPATH,
        "(//div[@class='home-hero-article-card']//div[2]//a[1])[4]")
    driver.execute_script("arguments[0].scrollIntoView();", initial_article)
    # actions = ActionChains(driver)
    # actions.move_to_element(article_heading).perform()
    article = initial_article.get_attribute("title")
    print("article is :", article)
    temp_heading = article + " - 21Ninety"
    driver.execute_script("arguments[0].click();", initial_article)
    print("clicked on article heading")
    WebDriverWait(driver, 20).until(ec.title_is(temp_heading))


def load_initial_article(driver):
    print("function called load_initial_article_of_most_popular")
    # tmp = driver.find_element(By.XPATH, "(//stn-player)[1]")
    # outer_root = driver.execute_script('return arguments[0].shadowRoot', tmp)
    # inner = outer_root.find_element(By.XPATH, "//div[@class='floatClose material-icons']")
    # inner.click()
    initial_article = driver.find_element(
        By.XPATH,
        "(//p[@class='article-card__title font-secondary'])[1]")
    title = initial_article.text
    print(title)
    tmp_str = "//a[@title='"+title+"']"
    tmp = driver.find_element(By.XPATH, tmp_str)
    # driver.execute_script("arguments[0].scrollIntoView();", initial_article)
    actions = ActionChains(driver)
    actions.move_to_element(initial_article).perform()
    tmp.click()
    WebDriverWait(driver, 40).until(ec.title_is(title+" - 21Ninety"))


def verify_injected_video(driver):
    print("function called verify_injected_video")
    # wait till the time main video screen is available
    WebDriverWait(driver, 15).until(ec.presence_of_element_located((
        By.XPATH, "(//div[@class='jwplayer image-wrapper image-wrapper--16x9'])[1]")))
    tmp = driver.find_elements(By.XPATH, "//button[@class='jwplayer__play bg-white color-at-green text-center']")
    if len(tmp) > 0:
        tmp_button_play = driver.find_element(
            By.XPATH,
            "//button[@class='jwplayer__play bg-white color-at-green text-center']")
        actions = ActionChains(driver)
        actions.move_to_element(tmp_button_play).perform()
        assert not tmp_button_play.is_displayed(), "Video is present but does not autoplay when in view"
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
        assert \
            author.is_displayed(), \
            "On Clicking Read Full Article button, Author is not displayed for article "+driver.title
