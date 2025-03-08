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


'''      
class TestElements:
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://practice-automation.com/form-fields/")

    def test_input_name(self,):
        try:
            result = 1 / 1
            assert result == None


        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")

    def test_input_password(self,):
        pass

    def test_drink_list(self,):
        pass

    def test_favorite_color(self,):
        pass

    def test_drop_list_estimation(self,):
        pass

    def test_input_email(self,):
        pass

    def test_input_message(self,):
        pass

    def test_press_button(self,):
        pass

if __name__ == "__main__":
    unittest.main()'''
