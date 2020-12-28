from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest


class test_class_name(unittest.TestCase):
    def test_calculator(self):
        link = "https://norma24.ru/"
        browser = webdriver.Chrome()
        browser.get(link)

        # разворачиваем окно на полный экран
        browser.maximize_window()

        # окрываем закладку Продукты
        product = browser.find_element_by_id("navbarDropdown")
        product.click()

        # выбираем банковские гарантии
        bg = browser.find_element_by_link_text("Банковские гарантии")
        bg.click()

        # промотка вниз до окна с калькулятором
        scroll = browser.find_element_by_id("calculator")
        browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)

        move = ActionChains(browser)

        # двигаем слайдер суммы гарантии
        slider_sum = browser.find_element_by_xpath(
            '/html/body/div[1]/div/section[4]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]')
        move.click_and_hold(slider_sum).move_by_offset(10, 0).release().perform()

        # двигаем слайдер срока гарантии
        slider_data = browser.find_element_by_xpath(
            '/html/body/div[1]/div/section[4]/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]')
        move.click_and_hold(slider_data).move_by_offset(150, 0).release().perform()

        summa_komissi = browser.find_element_by_class_name("choose-calc-subtitle")
        summa_komissi_text = summa_komissi.text

        assert summa_komissi_text == "8 705 935.34 ₽"


if __name__ == "__main__":
    unittest.main()