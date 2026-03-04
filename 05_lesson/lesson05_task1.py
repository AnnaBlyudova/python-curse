from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/classattr')


xpath_locator = (
    "//button[contains(concat(' ', normalize-space(@class), ' '), "
    "' btn-primary ')]"
)

search_button = driver.find_element(By.XPATH, xpath_locator)
search_button.click()

sleep(1)
driver.switch_to.alert.accept()

sleep(20)
