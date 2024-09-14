import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    header_checkout_page_locator = (By.XPATH,
                                    "//div[@class='page-title']/h1[contains(text(),'Welcome, Please Sign In!')]")

    checkout_as_guest = (By.XPATH, "//input[@value='Checkout as Guest']")
    edit_billing_address_input_locator = (By.XPATH, "//input[contains(@id, 'BillingNewAddress') and @type='text']")
    dropdown_country_locator = (By.ID, "BillingNewAddress_CountryId")
    country_option_locator = "//select[@id='BillingNewAddress_CountryId']/option[contains(text(),'{fcountryname}')]"
    continue_buttons_locator = "//div[@id='{fnamecontainer}-buttons-container']/input"
    check_money_order_locator = (By.ID, "paymentmethod_1")
    confirm_button = (By.XPATH, "//div[@id='confirm-order-buttons-container']/input[@value='Confirm']")
    successful_payment_text_locator = (By.XPATH, "//div[@class='section order-completed']/div[@class='title']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on checkout as guest button")
    def click_checkout_as_guest_button(self):
        self.click_element(self.find_element_by_locator(self.checkout_as_guest))

    @allure.step("Fill billing info")
    def fill_billing_info(self, text: str = 'test', country: str = 'United States'):
        billing_address_elements = self.find_elements_by_locator(self.edit_billing_address_input_locator)

        for element in billing_address_elements:
            self.wait_until_visible(element)
            element.send_keys(text)
            if 'Email' in element.get_attribute("id"):
                element.send_keys('@gmail.com')

        self.click_element(self.find_element_by_locator(self.dropdown_country_locator))
        self.click_element(self.find_element_by_locator((By.XPATH, self.country_option_locator.
                                                         format(fcountryname=country))))

    @allure.step("Click on continue button")
    def click_continue_button(self, name_container: str):
        self.click_element(self.find_element_by_locator(
            (By.XPATH, self.continue_buttons_locator.format(fnamecontainer=name_container))))

    @allure.step("Select check money order checkbox")
    def click_check_money_order_input(self):
        self.wait_implicitly()
        self.click_element(self.find_element_by_locator(self.check_money_order_locator))

    @allure.step("Click on confirm button")
    def click_confirm_button(self):
        self.click_element(self.find_element_by_locator(self.confirm_button))
