import random

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    register_form = (By.XPATH, "//form[@action='/register']")
    first_name_input = (By.ID, "FirstName")
    last_name_input = (By.ID, "LastName")
    email_input = (By.ID, "Email")
    password_input = (By.ID, "Password")
    confirm_password_input = (By.ID, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    gender_locators = (By.XPATH, "//input[@name='Gender']")
    result_text_locator = (By.XPATH, "//div[@class='page registration-result-page']//div[@class='result']")

    @allure.step("Fill out registration form")
    def fill_form(self, first_name, last_name, email, password):
        rndm = random.randint(0, 1)
        self.click_element(self.find_elements_by_locator(self.gender_locators)[rndm])
        self.send_keys(self.first_name_input, first_name)
        self.send_keys(self.last_name_input, last_name)
        self.send_keys(self.email_input, email)
        self.send_keys(self.password_input, password)
        self.send_keys(self.confirm_password_input, password)
        self.click_element(self.find_element_by_locator(self.register_button))
