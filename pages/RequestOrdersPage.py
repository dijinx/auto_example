from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from constants import user_constants


class RequestOrdersPage(BasePage):
    # пользователь открывает страницу заказов
    def open_request_orders(self):
        BasePage.open_site(self, user_constants.USER_PROD_REQUEST_ORDERS)

    # метод ниже забирает значение кадастрового номера из карточки заказа,
    # сравнивает с образцом,
    # при совпадении кликает по карточке
    # также при совпадении кликает по надписи "Подробнее" (тут только для пользователя)
    def click_on_request_card(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))
        if text == user_constants.USER_CADASTRAL_NUMBER_0:
            BasePage.click(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))
            BasePage.click(self, (By.XPATH, '//a[1][@class="order-card__action link"]'))

    # пользователь проверяет, что заказ отменён
    def check_request_status_is_denied(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="title_mini text_danger"]'))
        assert text == "запрос отменен"
        if text == "запрос отменен":
            print("Запрос отменён, тест пройден")

    # метод ниже забирает значение кадастрового номера из карточки заказа,
    # сравнивает с образцом,
    # при совпадении кликает по карточке
    # также при совпадении кликает по кнопке "Продолжить заказ" (тут только для пользователя)
    def click_on_request_card_btn_continue(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))
        if text == user_constants.USER_CADASTRAL_NUMBER_0:
            BasePage.click(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))
            BasePage.click(self, (By.XPATH, '//a/button[1]'))
