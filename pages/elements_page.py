# pages\elements_page.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

import time as tm


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('fill in all fields')

    def fill_all_fields(self):
        #print(self.driver.find_element(By.XPATH, self.locators.parsing_text_xpath).text)
        #print('________________________________')
        parse_lib_info = self.driver.find_element(By.XPATH, self.locators.parsing_text_xpath).text
        #
        max_symbol_word = max(parse_lib_info.split('\n'), key=len)
        parse_lib_info += f'\n\nСАМОЕ ДЛИННОЕ СИМВОЛЬНОЕ НА РАЙОНЕ:\n {max_symbol_word}'

        with allure.step('entering fields'):
            # Ввод полей
            self.driver.find_element(By.XPATH, self.locators.name_field_xpath).send_keys('Olivia')
            self.driver.find_element(By.XPATH, self.locators.password_field_xpath).send_keys('liv1moore')
            self.driver.find_element(By.XPATH, self.locators.email_field_xpath).send_keys('izombie@serial.com')
            self.driver.find_element(By.XPATH, self.locators.message_field_xpath).send_keys(parse_lib_info)

        with allure.step('select from the list'):
            # Выбор из списка
            element_milk_xpath = self.driver.find_element(By.XPATH, self.locators.drink_list_xpath_dict['milk_xpath'])
            self.driver.execute_script("arguments[0].click();", element_milk_xpath)

            element_coffee_xpath = self.driver.find_element(By.XPATH, self.locators.drink_list_xpath_dict['coffee_xpath'])
            self.driver.execute_script("arguments[0].click();", element_coffee_xpath)

            element_color = self.driver.find_element(By.XPATH, self.locators.color_list_xpath)
            self.driver.execute_script("arguments[0].click();", element_color)

            select_answer = Select(self.driver.find_element(By.XPATH, self.locators.drop_list_estimation_xpath))
            select_answer.select_by_visible_text('No')

        with allure.step('clicking on the button'):
            # Нажатие на кнопку
            element_submit_button = self.driver.find_element(By.XPATH, self.locators.submit_button_xpath)
            self.driver.execute_script("arguments[0].click();", element_submit_button)
