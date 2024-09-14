import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    title_of_product_locator = (By.XPATH, "//div[@class='search-results']//h2[@class='product-title']/a")
    header_founded_product_locator = (By.XPATH, "//div[@class='page-title']/h1[contains(text(),'Search')]")
    add_cart_button_locator = (By.XPATH, "//input[@value='Add to cart']")
    notification_bar_locator = (By.XPATH, "//div[@id='bar-notification']/p[@class='content']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on add cart")
    def click_add_to_cart_button(self):
        self.click_element(self.find_element_by_locator(self.add_cart_button_locator))
