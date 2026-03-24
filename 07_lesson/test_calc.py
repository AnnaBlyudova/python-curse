from selenium import webdriver
from page.calculator import Calculator
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calc = Calculator(driver)

    calc.set_delay()
    calc.add_numbers()
    calc.wait_for_result()

    result_text = calc.get_result_text()
    assert result_text == '15'
