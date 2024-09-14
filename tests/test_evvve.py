import allure
from faker import Faker
from selenium.webdriver.chrome.webdriver import WebDriver

from conftest import navigate_to_cart
from tests.test_data import SEARCH_VALUE

faker = Faker()


@allure.id("TC01")
@allure.description("Verify that a new user can register successfully.")
def test_successful_registration(driver: WebDriver, navigate_to_demowebshop):
    main_page = navigate_to_demowebshop
    assert main_page.page_is_displayed(main_page.main_page_content), 'The main page should be displayed'

    register_page = main_page.click_register_link()
    assert register_page.page_is_displayed(register_page.register_form), 'The register form should be displayed'

    register_page.fill_form(first_name=faker.first_name(),
                            last_name=faker.last_name(),
                            email=faker.email(),
                            password=faker.password())

    assert (register_page.get_text(register_page.result_text_locator) == "Your registration completed"), \
        'Registration is not completed'


@allure.id("TC02")
@allure.description("Verify that searching for a product displays relevant results.")
def test_successful_searching_of_product(driver: WebDriver, navigate_to_demowebshop):
    main_page = navigate_to_demowebshop
    assert main_page.page_is_displayed(main_page.main_page_content), 'The main page should be displayed'

    product_page = main_page.fill_search_field(SEARCH_VALUE)
    assert product_page.page_is_displayed(product_page.header_founded_product_locator), \
        'The product page should be displayed'

    assert SEARCH_VALUE in product_page.get_text(product_page.title_of_product_locator), 'The product is not displayed'


@allure.id("TC03")
@allure.description("Verify that a user can add a product to the shopping cart.")
def test_successful_adding_in_shopping_cart(driver: WebDriver, navigate_to_demowebshop):
    main_page = navigate_to_demowebshop
    assert main_page.page_is_displayed(main_page.main_page_content), 'The main page should be displayed'

    product_page = main_page.fill_search_field(SEARCH_VALUE)
    product_page.click_add_to_cart_button()
    assert (product_page.get_text(product_page.notification_bar_locator) ==
            "The product has been added to your shopping cart"), \
        'The notification bar is not displayed'

    shopping_cart_page = navigate_to_cart(driver)
    assert shopping_cart_page.page_is_displayed(shopping_cart_page.header_shopping_cart_page), \
        'The shopping page should be displayed'

    assert SEARCH_VALUE in shopping_cart_page.get_text(shopping_cart_page.name_of_product_locator), \
        'The product is not matched'


@allure.id("TC04")
@allure.description("Verify that a user can complete the checkout process.")
def test_successful_checkout(driver: WebDriver, navigate_to_demowebshop):
    main_page = navigate_to_demowebshop
    assert main_page.page_is_displayed(main_page.main_page_content), 'The main page should be displayed'

    product_page = main_page.fill_search_field(SEARCH_VALUE)
    product_page.click_add_to_cart_button()
    assert (product_page.get_text(product_page.notification_bar_locator) ==
            "The product has been added to your shopping cart"), \
        'The notification bar is not displayed'

    shopping_cart_page = navigate_to_cart(driver)
    assert shopping_cart_page.page_is_displayed(shopping_cart_page.header_shopping_cart_page), \
        'The shopping page should be displayed'

    assert SEARCH_VALUE in shopping_cart_page.get_text(shopping_cart_page.name_of_product_locator), \
        'The product is not matched'

    shopping_cart_page.click_checkbox_agreement()
    checkout_page = shopping_cart_page.click_checkout_button()
    assert checkout_page.page_is_displayed(checkout_page.header_checkout_page_locator), \
        'The checkout page should be displayed'

    checkout_page.click_checkout_as_guest_button()
    checkout_page.fill_billing_info()

    checkout_page.click_continue_button('billing')

    checkout_page.click_continue_button('shipping')

    checkout_page.click_continue_button('shipping-method')

    checkout_page.click_check_money_order_input()

    checkout_page.click_continue_button('payment-method')

    checkout_page.click_continue_button('payment-info')

    checkout_page.click_confirm_button()
    assert (checkout_page.get_text(checkout_page.successful_payment_text_locator)
            == "Your order has been successfully processed!"), 'Payment message not displayed'
