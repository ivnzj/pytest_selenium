from tests.ui.selectors import GoogleSelectors
from tests.ui.timeouts import wait_until_present
from tests.ui.pages.base_page import BasePage

class GoogleResultsPage(BasePage):
    def wait_for_results(self):
        wait_until_present(self.driver, GoogleSelectors.SEARCH_RESULTS_SECTION)

    def get_top_results(self):
        """Retrieve the top search results."""
        return [
            result for result in self.driver.find_elements(*GoogleSelectors.SEARCH_RESULT_BLOCKS)
            if result.find_elements(*GoogleSelectors.SEARCH_RESULT_TITLE)
            and result.find_elements(*GoogleSelectors.SEARCH_RESULT_LINK)
        ]

    def print_top_results(self, results, count=5):
        """Print the top search results."""
        print(f"\nTop {count} Google Search Results:\n")
        for idx, result in enumerate(results[:count], start=1):
            try:
                title = result.find_element(*GoogleSelectors.SEARCH_RESULT_TITLE).text.strip()
                link = result.find_element(*GoogleSelectors.SEARCH_RESULT_LINK).get_attribute("href")
                print(f"{idx}. {title}\n   {link}\n")
            except:
                print(f"{idx}. [Unable to extract title or link]")
