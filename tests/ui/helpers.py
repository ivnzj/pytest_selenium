import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.ui.constants import COOKIES_FILE
from tests.ui.selectors import GoogleSelectors
from tests.ui.timeouts import wait_until_present


def save_cookies(driver, path=COOKIES_FILE):
    with open(path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, path=COOKIES_FILE):
    with open(path, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            cookie.pop("expiry", None)
            driver.add_cookie(cookie)

def wait_if_captcha_present(driver):
    try:
        wait_until_present(driver, GoogleSelectors.CAPTCHA_IFRAME, timeout=3)
        print("CAPTCHA iframe detected. Please solve it manually.")
        print("Waiting for search results to appear...")
        wait_until_present(driver, GoogleSelectors.SEARCH_RESULTS_SECTION, timeout=120)
        return
    except:
        pass

    if "unusual traffic" in driver.title.lower() or "captcha" in driver.page_source.lower():
        print("CAPTCHA page detected. Please solve it manually.")
        print("Waiting for search results to appear...")
        wait_until_present(driver, GoogleSelectors.SEARCH_RESULTS_SECTION, timeout=120)

