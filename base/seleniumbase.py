from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:

    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_function_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        elements = {
            'css': By.CSS_SELECTOR,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'xpath': By.XPATH,
            'name': By.NAME,
            'tag_name': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link': By.PARTIAL_LINK_TEXT
        }
        return elements[find_by]
