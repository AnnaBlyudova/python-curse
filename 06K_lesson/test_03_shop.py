from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    input_name = driver.find_element(By.ID, 'user-name')
    input_name.send_keys('standard_user')

    input_pass = driver.find_element(By.ID, 'password')
    input_pass.send_keys('secret_sauce')

    driver.find_element(By.ID, 'login-button').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-backpack')))

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    input_first_name = driver.find_element(By.ID, 'first-name')
    input_first_name.send_keys('Анна')

    input_last_name = driver.find_element(By.ID, 'last-name')
    input_last_name.send_keys('Блюдова')

    input_index = driver.find_element(By.ID, 'postal-code')
    input_index.send_keys('085013')

    driver.find_element(By.ID, 'continue').click()

    result_price = driver.find_element(
        By.CSS_SELECTOR, '.summary_total_label').text
    assert '$58.29' in result_price

    driver.quit()
