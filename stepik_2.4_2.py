from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))


book = browser.find_element_by_css_selector('.container .btn')
book.click()

scroll = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)

x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = int(x)

num = math.log(abs(12*math.sin(y)))
num_t = str(num)

rez = browser.find_element_by_id("answer")
rez.send_keys(num_t)

button_2 = browser.find_element_by_id('solve')
button_2.click()