from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_troll = browser.find_element_by_css_selector('.container .trollface')
button_troll.click()

new_window = browser.window_handles[1]#определили имя новой вклдаки
browser.switch_to.window(new_window)#переключились на новую вкладку для работы

x_element = browser.find_element_by_id("input_value")
#x_element = browser.find_element_by_xpath('/html/body/form/div/div/div/label/span[2]')
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
