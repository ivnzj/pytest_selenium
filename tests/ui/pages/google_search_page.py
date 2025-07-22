from tests.ui.selectors import GoogleSelectors
from tests.ui.timeouts import wait_for_clickable, wait_until_present
from tests.ui.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage(BasePage):
    def go_to(self):
        self.driver.get("https://www.google.com")

    def accept_cookies_if_needed(self):
        """Accept cookies if the consent button is present."""
        try:
            consent_button = wait_for_clickable(self.driver, GoogleSelectors.ACCEPT_COOKIES_BTN)
            self.click_with_random_delay(consent_button)
        except:
            pass

    def enter_search_query(self, query):
        """Enter a search query into the Google search input."""
        search_input = wait_until_present(self.driver, GoogleSelectors.SEARCH_INPUT)
        search_input.clear()
        self.slow_send_keys(search_input, query)

    def click_search(self):
        """Click the search button."""
        search_button = wait_for_clickable(self.driver, GoogleSelectors.SEARCH_BUTTON)
        self.click_with_random_delay(search_button)
