import time
import random

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_with_random_delay(self, element):
        """Click an element with a random delay to mimic human interaction."""
        time.sleep(random.uniform(0.3, 0.46))
        element.click()

    def slow_send_keys(self, element, text):
        """Send keys to an element with a delay between each character."""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.15, 0.3))
