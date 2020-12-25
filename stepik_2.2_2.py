from selenium import webdriver
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    y = int(x)

    num = math.log(abs(12*math.sin(y)))
    num_t= str(num)

    scroll = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)

    scroll.send_keys(num_t)

    chekb = browser.find_element_by_id("robotCheckbox")
    chekb.click()

    radio_off = browser.find_element_by_id("peopleRule")
    radio_off.click()

    radio_on = browser.find_element_by_id("robotsRule")
    radio_on.click()

    button = browser.find_element_by_css_selector('.container .btn')
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла