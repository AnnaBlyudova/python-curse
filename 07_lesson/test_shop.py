from selenium import webdriver
from page.autoriz import LoginPage
from page.products import Products
from page.cart import Card
from page.checkout_page import CheckoutPage
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    name = LoginPage(driver)
    name.autorization('standard_user', 'secret_sauce')

    product = Products(driver)
    product.add_to_card()

    cart = Card(driver)
    cart.click_checkout()

    full_form = CheckoutPage(driver)
    full_form.adress('Анна', 'Блюдова', '085013')

    result_price = driver.find_element(
        By.CSS_SELECTOR, '.summary_total_label').text
    assert '$58.29' in result_price
