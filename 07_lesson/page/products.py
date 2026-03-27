from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Products():
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'add-to-cart-sauce-labs-backpack')))

    def add_to_card(self):
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
        return self
