from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('.bg-light .btn')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = int(x)

num = math.log(abs(12*math.sin(y)))
num_t = str(num)

rez = browser.find_element_by_id("answer")
rez.send_keys(num_t)

button_2 = browser.find_element_by_css_selector('.container .btn')
button_2.click()

time.sleep(10)
browser.quit()

