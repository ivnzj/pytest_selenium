import os
from tests.ui.pages.google_search_page import GoogleSearchPage
from tests.ui.pages.google_results_page import GoogleResultsPage
from tests.ui.constants import COOKIES_FILE
from tests.ui.helpers import save_cookies, load_cookies, wait_if_captcha_present

def test_google_search_synot_games(driver):
    search_page = GoogleSearchPage(driver)
    results_page = GoogleResultsPage(driver)

    search_page.go_to()

    if os.path.exists(COOKIES_FILE):
        load_cookies(driver)
        driver.refresh()
    else:
        search_page.accept_cookies_if_needed()
        save_cookies(driver)

    search_page.enter_search_query("synot games")
    search_page.click_search()
    wait_if_captcha_present(driver)

    results_page.wait_for_results()
    results = results_page.get_top_results()

    assert results, "No search results were found."
    results_page.print_top_results(results)

    found = any("synot games" in result.text.lower() for result in results[:5])
    assert found, "No top result contains the term 'synot games'."
