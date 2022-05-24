import time

from pages.BasePage import BasePage
from constants import user_constants
from selenium.webdriver.common.by import By


class StartPage(BasePage):

    # пользователь заходит на сайт без авторизации
    def open_main_page(self):
        BasePage.open_site(self, user_constants.USER_PROD_MAIN_PAGE)

    # пользователь авторизуется
    def login(self):
        BasePage.user_auth(self)

    # пользователь открывает страницу авторизации
    def open_authorization_page(self):
        BasePage.open_site(self, user_constants.USER_PROD_MAIN_PAGE)

    # пользователь нажимает кнопку "Войти"
    def press_button_enter(self):
        BasePage.click(self,
                       (By.CLASS_NAME, 'profile-widget'))

    # пользователь проверяет адрес страницы после авторизации
    # после авторизации пользователь попадает на страницу favorites
    def url_checking(self):
        text = BasePage.get_url(self)
        print(text)
        assert text == user_constants.USER_PROD_FAVORITES_PAGE
        if text == user_constants.USER_PROD_FAVORITES_PAGE:
            print('Пользователь успешно авторизовался!')

    # пользователь нажимает кнопку "нужна консультация"
    def user_click_btn_need_consultation(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="el-button el-button--primary el-button--small home-banner__btn-consult"]'))
        time.sleep(3)

    # пользователь вводит имя в форме обратной связи
    def user_enter_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@data-test-id="name-input"]'), 'TEST')

    # пользователь вводит номер телефона в форме обратной связи
    def user_enter_phone(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@data-test-id="phone-input"]'), '1234567890')

    # пользователь вводит почту в форме обратной связи
    def user_enter_email(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@data-test-id="email-input"]'), '01.01.test@mail.ru')

    # пользователь вводит сообщение в форме обратной связи
    def user_enter_notification_text(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@data-test-id="message-input"]'), 'TEST Message')

    # пользователь нажимает кнопку отправить в форме обратной связи
    def user_click_btn_send(self):
        BasePage.click(self, (By.XPATH, '//*[@data-test-id="submit-button"]'))

    # пользователь проверяет, что сообщение отправилось
    def user_check_notification_is_send(self):
        text = BasePage.get_text(self, (By.XPATH, '/html/body/div[3]/div/div[1]'))
        print(text)
        assert text == 'В течение двух часов с вами свяжется наш менеджер'
        if text == 'В течение двух часов с вами свяжется наш менеджер':
            print('Сообщение отправлено')
