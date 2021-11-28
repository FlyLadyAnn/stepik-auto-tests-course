from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_text_on_button_add_to_card(browser):
    browser.get(link)
    time.sleep(30)

    # формируется список подходящих элементов, но т.к. селектор уникальный, то будет 1 элемент
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    # если кол-во =0, то элемента нет на странице
    assert len(buttons) != 0, "Button is missing on the page"


