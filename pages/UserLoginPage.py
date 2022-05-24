from selenium.webdriver.common.by import By

from constants import user_constants
from pages.BasePage import BasePage


class UserLogin(BasePage):

    # пользователь вводит телефонный номер
    def enter_phone(self):
        BasePage.send_keys(self, (By.ID, 'phoneInput'), user_constants.USER_AUTHORIZATION_PHONE_NUMBER)

    # пользователь нажимает кнопку "Далее"
    def press_button_next(self):
        BasePage.click(self, (By.CLASS_NAME, 'button__content'))

    # пользователь вводит пароль
    def enter_password(self):
        BasePage.send_keys(self, (By.ID, 'password'), user_constants.USER_AUTHORIZATION_PASSWORD)
