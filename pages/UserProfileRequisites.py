import time

from selenium.webdriver.common.by import By

from constants import user_constants
from pages.BasePage import BasePage


class UserProfileRequisites(BasePage):
    # пользователь заходит на страницу платёжных реквизитов в профиле
    def user_open_requisites_page(self):
        BasePage.open_site(self, user_constants.USER_PROD_REQUISITES)

    # пользователь авторизуется
    def new_user_auth(self):
        BasePage.user_auth_new_user_for_profile_and_requisites(self)

    # пользователь нажимает кнопку добавить
    def user_click_btn_add(self):
        BasePage.click(self, (By.XPATH, '//*[1][@class="el-button el-button--primary el-button--small"]'))

    # пользователь вносит название счёта
    def user_fill_requisites_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Основной расчётный счёт"]'),
                           user_constants.USER_REQUISITES_NAME)

    # пользователь вносит бик
    def user_fill_bik(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="000000000"]'), user_constants.USER_REQUISITES_BIK)

    # пользователь вносит наименование банка
    def user_fill_bank_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Наименование банка"]'),
                           user_constants.USER_REQUISITES_BANK_NAME)

    # пользователь вносит адрес
    def user_fill_address(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Россия, 115432, г. Москва, Андропова пр-т, д. 18"]'),
                           user_constants.USER_REQUISITES_ADDRESS)

    # пользователь вносит КС
    def user_fill_ks(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div/div/main/main/div/div[2]/div[1]/div[3]/div/div[2]/form/div[5]/div/div[1]/input'),
                           user_constants.USER_REQUISITES_KS)

    # пользователь вносит РС
    def user_fill_rs(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div/div/main/main/div/div[2]/div[1]/div[3]/div/div[2]/form/div[6]/div/div[1]/input'),
                           user_constants.USER_REQUISITES_RS)

    # пользователь нажимает кнопку "сохранить"
    def user_click_btn_save(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div/div/main/main/div/div[2]/div[1]/div[3]/div/div[3]/div/button[2]'))

    # пользователь проверяет что, реквизиты сохранились
    def user_check_requisites_is_save(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="el-notification__content"]'))
        print(text)
        assert text == user_constants.USER_REQUISITES_IS_SAVE_PUSH_TEXT
        if text == user_constants.USER_REQUISITES_IS_SAVE_PUSH_TEXT:
            print('Реквизиты успешно сохранены!')

    # пользователь удаляет реквизиты
    def user_delete_requisites(self):
        BasePage.click(self, (By.XPATH, '//*[2][@class="el-button el-button--info el-button--small"]'))
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div/div/main/main/div/div[2]/div[1]/div[4]/div/div[3]/div/button[2]'))

    # пользователь проверяет , что реквизиты удалены
    def user_check_requisites_is_delete(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="el-notification__content"]'))
        print(text)
        # assert text == user_constants.USER_REQUISITES_IS_DELETE_PUSH_TEXT
        # if text == user_constants.USER_REQUISITES_IS_DELETE_PUSH_TEXT:
        print('Реквизиты удалены!')

    # пользователь проверяет название счета
    def user_check_requisites_name(self):
        value = BasePage.get_text(self, (By.XPATH, '//*[@title="Акционерное общество «Тинькофф Банк»"]'))
        assert value == user_constants.USER_REQUISITES_NAME
        if value == user_constants.USER_REQUISITES_NAME:
            print(
                'Ожидаемое имя реквизитов: ' + user_constants.USER_REQUISITES_NAME + '\n' + 'Имя в карточке: ' + value)

    # пользователь проверяет бик
    def user_check_bik(self):
        value = BasePage.get_text(self, (By.XPATH, '//*[@title="044525974"]'))
        assert value == user_constants.USER_REQUISITES_BIK
        if value == user_constants.USER_REQUISITES_BIK:
            print('Ожидаемый БИК: ' + user_constants.USER_REQUISITES_BIK + '\n' + 'БИК в карточке: ' + value)
        time.sleep(3)

    # пользователь проверяет наименование банка
    def user_check_bank_name(self):
        value = BasePage.get_text(self, (By.XPATH, '//*[@title="АО «Тинькофф Банк»"]'))
        assert value == user_constants.USER_REQUISITES_BANK_NAME
        if value == user_constants.USER_REQUISITES_BANK_NAME:
            print('Ожидаемое имя банка: '
                  + user_constants.USER_REQUISITES_BANK_NAME
                  + '\n' + 'Имя банка в карточке: ' + value)
        time.sleep(3)

    # пользователь проверяет адрес
    def user_check_address(self):
        value = BasePage.get_text(self, (
            By.XPATH, '//*[@title="Москва, 127287, ул. Хуторская 2-я, д. 38А, стр. 26;а/я 23, г. Москва, 102001"]'))
        assert value == user_constants.USER_REQUISITES_ADDRESS
        if value == user_constants.USER_REQUISITES_ADDRESS:
            print('Ожидаемый адрес: ' + user_constants.USER_REQUISITES_ADDRESS + '\n' + 'Адрес в карточке: ' + value)

    # пользователь проверяет КС
    def user_check_ks(self):
        value = BasePage.get_text(self, (By.XPATH, '//*[@title="30101810145250000974"]'))
        assert value == user_constants.USER_REQUISITES_KS
        if value == user_constants.USER_REQUISITES_KS:
            print('Ожидаемый КС: ' + user_constants.USER_REQUISITES_KS + '\n' + 'КС в карточке: ' + value)

    # пользователь проверяет РС
    def user_check_rs(self):
        value = BasePage.get_text(self, (By.XPATH, '//*[@title="30232810100000000004"]'))
        assert value == user_constants.USER_REQUISITES_RS
        if value == user_constants.USER_REQUISITES_RS:
            print('Ожидаемый РС: ' + user_constants.USER_REQUISITES_RS + '\n' + 'РС в карточке: ' + value)
