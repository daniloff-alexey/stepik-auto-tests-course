from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://norma24.ru/')

xpath = '/html/body/div[1]/header/div/div/nav/div/div/a'
button = browser.find_element_by_xpath(xpath).click()

xpath_login = '/html/body/div[1]/div/section/div/div/div/div/div[1]/div/form/div[1]/input'
browser.find_element_by_xpath(xpath_login).send_keys('8800200600')

xpath_password = '/html/body/div[1]/div/section/div/div/div/div/div[1]/div/form/div[2]/input'
browser.find_element_by_xpath(xpath_password).send_keys('8800200600')

xpath_button = '/html/body/div[1]/div/section/div/div/div/div/div[1]/div/form/div[3]/button'
browser.find_element_by_xpath(xpath_button).click()

