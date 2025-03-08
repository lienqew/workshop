import time

import allure
#import pytest

from pages.elements_page import TextBoxPage


@allure.suite('Elements')
class TestElements:
    @allure.title('check textbox')
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://practice-automation.com/form-fields/')
        text_box_page.open()
        text_box_page.fill_all_fields()
        time.sleep(5)
        assert True
