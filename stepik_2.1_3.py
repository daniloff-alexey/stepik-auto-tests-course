from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    element_vvod = browser.find_element_by_id("answer")
    element_vvod.send_keys(y)

    chekb = browser.find_element_by_id("robotCheckbox")
    chekb.click()

    radio_on = browser.find_element_by_id("peopleRule")
    radio_on.click()

    radio_of = browser.find_element_by_id("robotsRule")
    radio_of.click()

    button = browser.find_element_by_css_selector('.container .btn')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()