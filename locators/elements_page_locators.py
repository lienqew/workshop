# locators\elements_page_locators.py
from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    '''Поля ввода'''
    name_field_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/label[1]/input"
    password_field_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/label[2]/input"
    email_field_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/input[11]"
    message_field_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/textarea"

    '''Списки'''
    drink_list_xpath_dict = {'milk_xpath': "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/input[2]",
                             'coffee_xpath': "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/input[3]"}

    color_list_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/input[8]"
    drop_list_estimation_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/select"

    '''Кнопка'''
    submit_button_xpath = "/html/body/div[1]/div[2]/div/div/main/div/article/div/form/button"

    '''Элемент дял парсинга'''
    parsing_text_xpath = '/html/body/div[1]/div[2]/div/div/main/div/article/div/form/ul'
