from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    ADD_TO_BASKET_BUTTON = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert ADD_TO_BASKET_BUTTON is not None, "Кнопка добавления в корзину не найдена"