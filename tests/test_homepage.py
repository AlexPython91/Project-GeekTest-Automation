import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_auth_homepage(self):
        driver = webdriver.Chrome
        driver.implicitly_wait(10)

        wait = WebDriverWait(driver, 10)
        name_input_field = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'mdc-text-field__input')))

