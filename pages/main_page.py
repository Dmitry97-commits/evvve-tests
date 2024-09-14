import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage


class MainPage(BasePage):
    main_page_content = (By.XPATH, "//div[@class='master-wrapper-main']")
    register_link = (By.XPATH, "//div[@class='header-links']//a[@class='ico-register']")
    search_field = (By.ID, "small-searchterms")
    search_button = (By.XPATH, "//input[@value='Search']")
    continue_button = (By.XPATH, "//input[@title='Continue']")

    @allure.step("Click on register link")
    def click_register_link(self):
        self.click_element(self.find_element_by_locator(self.register_link))
        return RegisterPage(self.driver)

    @allure.step("Fill search field")
    def fill_search_field(self, text):
        self.send_keys(self.search_field, text)
        self.click_element(self.find_element_by_locator(self.search_button))
        return ProductPage(self.driver)
