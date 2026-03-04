from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/login')

search_input_name = driver.find_element(By.CSS_SELECTOR, '#username')
search_input_name.send_keys("tomsmith")

search_input = driver.find_element(By.CSS_SELECTOR, '#password')
search_input.send_keys("SuperSecretPassword!")

sleep(2)
search_button_login = driver.find_element(By.CSS_SELECTOR, '.radius')
search_button_login.click()

flash = driver.find_element(By.CSS_SELECTOR, '#flash')
print(flash.text)

driver.quit()
