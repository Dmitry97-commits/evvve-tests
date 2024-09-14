import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Find element by locator")
    def find_element_by_locator(self, locator: tuple):
        return self.driver.find_element(*locator)

    @allure.step("Find elements by locator")
    def find_elements_by_locator(self, locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step("Check page is displayed")
    def page_is_displayed(self, locator: tuple):
        return self.find_element_by_locator(locator).is_displayed()

    @allure.step("Get text")
    def get_text(self, locator: tuple):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        return self.find_element_by_locator(locator).text

    @allure.step("Wait until visible element")
    def wait_until_visible(self, locator: tuple):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(locator))

    @allure.step("Wait implicitly")
    def wait_implicitly(self, sec: int = 5):
        self.driver.implicitly_wait(sec)

    def click_element(self, element: WebElement):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(element))
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element))
        element.click()

    def send_keys(self, locator: tuple, keys: str):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        self.find_element_by_locator(locator).send_keys(keys)
