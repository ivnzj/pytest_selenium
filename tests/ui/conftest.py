import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import USER_AGENTS

@pytest.fixture
def driver():
    user_agent = random.choice(USER_AGENTS)
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
