from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

f_name = browser.find_element_by_name("firstname")
f_name.send_keys("Ivan")

l_name = browser.find_element_by_name("lastname")
l_name.send_keys("Ivanov")

e_mail = browser.find_element_by_name("email")
e_mail.send_keys("pochta@pochta.ru")

current_dir = os.path.abspath(os.path.dirname('__file__'))
file_path = os.path.join(current_dir, 'zagruzka.txt')
element = browser.find_element_by_name("file")
element.send_keys(file_path)

button = browser.find_element_by_css_selector('.container .btn')
button.click()

time.sleep(10)
browser.quit()
