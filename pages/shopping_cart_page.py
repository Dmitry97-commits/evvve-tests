import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class ShoppingCartPage(BasePage):
    header_shopping_cart_page = (By.XPATH, "//div[@class='page-title']/h1[contains(text(),'Shopping cart')]")
    name_of_product_locator = (By.XPATH, "//tr[@class='cart-item-row']//td[@class='product']/a")
    checkout_button_locator = (By.ID, "checkout")
    agreement_checkbox_locator = (By.ID, "termsofservice")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on checkout button")
    def click_checkout_button(self):
        self.click_element(self.find_element_by_locator(self.checkout_button_locator))
        return CheckoutPage(self.driver)

    @allure.step("Click on checkbox for agreement")
    def click_checkbox_agreement(self):
        self.click_element(self.find_element_by_locator(self.agreement_checkbox_locator))
