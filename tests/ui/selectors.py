from selenium.webdriver.common.by import By

class GoogleSelectors:
    ACCEPT_COOKIES_BTN = (By.XPATH, "//button[contains(., 'Prijať všetko')]")
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    SEARCH_RESULTS_SECTION = (By.ID, "search")
    SEARCH_RESULT_BLOCKS = (By.CSS_SELECTOR, "div#search .tF2Cxc")
    SEARCH_RESULT_TITLE = (By.TAG_NAME, "h3")
    SEARCH_RESULT_LINK = (By.TAG_NAME, "a")
    CAPTCHA_IFRAME = (By.XPATH, "//iframe[contains(@src, 'recaptcha')]")