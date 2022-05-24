import time

from selenium.webdriver.common.keys import Keys

from constants import user_constants
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class UserProfileOrganizationPage(BasePage):
    # авторизация нового пользователя
    def user_auth_new_user(self):
        BasePage.user_auth_new_user(self)

    # пользователь открывает страницу "Моя организация"
    def open_organization(self):
        BasePage.open_site(self, user_constants.USER_PROD_ORGANIZATION_PAGE)

    # пользователь проверяет ссылку страницы, должна быть https://estate.mts.ru/profile/organization
    def check_url_is_profile_organization_user(self):
        url = BasePage.get_url(self)
        assert url == user_constants.USER_PROD_ORGANIZATION_PAGE
        if url == user_constants.USER_PROD_ORGANIZATION_PAGE:
            print('URL верный.')
        time.sleep(3)

    # проверка наименование организации
    def check_org_name(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(2)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_LEGAL_NAME
        if value == user_constants.USER_CHECK_ORG_LEGAL_NAME:
            print('Наименование организации корректное')

    # проверка типа владения
    def check_type_ownership_org(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(1)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_TYPE_OWNERSHIP
        if value == user_constants.USER_ORG_TYPE_OWNERSHIP:
            print('Тип владения корректный')

    # пользователь вводит ИНН
    def user_fill_inn(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="000000000000"]'), user_constants.USER_ORG_INN)

    # проверка ИНН
    def check_org_inn(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(3)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_INN
        if value == user_constants.USER_CHECK_ORG_INN:
            print('ИНН корректный')

    # пользователь вводит КПП
    def user_fill_kpp(self):
        BasePage.send_keys(self,
                           (By.XPATH, '//*[@placeholder="000000000"]'), user_constants.USER_ORG_KPP)

    # проверка КПП
    def check_org_kpp(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(5)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_KPP
        if value == user_constants.USER_CHECK_ORG_KPP:
            print('КПП корректный')

    # пользователь нажимает кнопку Загрузить данные
    def click_btn_load_data(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR, '[data-a-test-id="btn_load_data"]'))

    # пользователь вводить фамилию
    def user_fill_org_last_name(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            '[data-test-id="org-form-last-name"]'), user_constants.USER_LAST_NAME)

    # пользователь вводить имя
    def user_fill_org_first_name(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            '[data-test-id="org-form-first-name"]'), user_constants.USER_FIRST_NAME)

    # пользователь вводить отчество
    def user_fill_org_second_name(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            '[data-test-id="org-form-second-name"]'), user_constants.USER_SECOND_NAME)

    # пользователь вносит электронную почту
    def user_fill_org_reg_email(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            '[data-test-id="org-form-email"]'), user_constants.USER_MAIL)

    # пользователь загружает архив с документами подтверждающими представительство организации
    def load_org_document_archive(self):
        BasePage.load_file(self,
                           (By.XPATH,
                            '//input[@accept=".zip, .rar"]'), user_constants.USER_ORG_DOCUMENT_ARCHIVE)

    # пользователь нажимает чекбокс с текстом
    # Нажимая "Сохранить данные" я даю согласие на обработку персональных данных
    def click_checkbox_org_save_data(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR, '[class="el-checkbox__inner"]'))

    # пользователь нажимает кнопку "Отправить заявку"
    def click_btn_send_request(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR,
                        '[class="page-content"]>[class="el-button el-button--primary el-button--small"]'))

    # ждем сообщения 'Данные организации обновлены'
    # проверяем, что данные успешно сохранены
    def check_request_update_org_accepted(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR, 'div>div>div.el-notification__content>p'))
        assert text == 'Данные организации обновлены'
        if text == 'Данные организации обновлены':
            print("Пользователь видит сообщение об успешном обновлении данных организации")

    # пользователь нажимает кнопку "Редактировать" данные организации
    def click_btn_org_edit(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR,
                        '[class="el-button organization__button el-button--primary el-button--small"]'))
        time.sleep(2)

    # пользователь вносит ОГРН
    def user_fill_ogrn(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(1)>form>div>div:nth-child(4)>div>div>div.el-input>input'),
                           user_constants.USER_ORG_OGRN)

    # пользователь проверяет ОГРН
    def check_org_ogrn(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(4)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_OGRN
        if value == user_constants.USER_CHECK_ORG_OGRN:
            print('ОГРН корректный')

    # пользователь вносит ОКТМО
    def user_fill_oktmo(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(1)>form>div>div:nth-child(6)>div>div>div>input'),
                           user_constants.USER_ORG_OKTMO)
        time.sleep(3)

    # пользователь проверяет ОКТМО
    def check_org_oktmo(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(6)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_OKTMO
        if value == user_constants.USER_CHECK_ORG_OKTMO:
            print('ОКТМО корректный')

    # пользователь вносит ОКАТО
    def user_fill_okato(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(1)>form>div>div:nth-child(7)>div>div>div>input'),
                           user_constants.USER_ORG_OKATO)

    # пользователь проверяет ОКАТО
    def check_org_okato(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(1)>div>div:nth-child(7)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_OKATO
        if value == user_constants.USER_CHECK_ORG_OKATO:
            print('ОКАТО корректный')

    # пользователь вносит телефон
    def user_fill_org_phone(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(2)>form>div>div:nth-child(1)>div>div>div>input'),
                           user_constants.USER_CHECK_ORG_PHONE)

    # пользователь проверяет телефон
    def check_org_phone(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(2)>div>div:nth-child(1)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_PHONE
        if value == user_constants.USER_CHECK_ORG_PHONE:
            print('Телефон корректный')

    # пользователь вносит email
    def user_fill_org_email(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(2)>form>div>div:nth-child(2)>div>div>div>input'),
                           user_constants.USER_ORG_REG_MAIL)

    # пользователь проверяет email
    def check_org_email(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(2)>div>div:nth-child(2)>p.organization-info__value'))
        assert value == user_constants.USER_CHECK_ORG_MAIL
        if value == user_constants.USER_CHECK_ORG_MAIL:
            print('EMail корректный')

    # пользователь вносит регион
    def user_fill_org_region(self):
        BasePage.send_keys(self, (By.CSS_SELECTOR, '[placeholder="Выбрать"]'), 'Москва')
        BasePage.click(self, (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[77]'))

    # пользователь проверяет регион юр.адреса
    def check_org_region_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(1)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_CITY
        if value == user_constants.USER_ORG_CITY:
            print('Регион юр.адреса корректный')

    # пользователь проверяет регион факт.адреса
    def check_org_region_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(1)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_CITY
        if value == user_constants.USER_ORG_CITY:
            print('Регион факт.адреса корректный')

    # пользователь вносит город
    def user_fill_org_city(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(3)>form>div>div:nth-child(2)>div>div>div.el-input>input'),
                           user_constants.USER_ORG_CITY)

    # пользователь проверяет город юр.адреса
    def check_org_city_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(2)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_CITY
        if value == user_constants.USER_ORG_CITY:
            print('Город юр.адреса корректный')

    # пользователь проверяет город факт.адреса
    def check_org_city_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(2)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_CITY
        if value == user_constants.USER_ORG_CITY:
            print('Город факт.адреса корректный')

    # пользователь вносит индекс
    def user_fill_org_index(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(3)>form>div>div:nth-child(3)>div>div>div.el-input>input'),
                           user_constants.USER_ORG_INDEX)

    # пользователь проверяет индекс юр.адреса
    def check_org_index_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(3)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_INDEX
        if value == user_constants.USER_ORG_INDEX:
            print('Индекс юр.адреса корректный')

    # пользователь проверяет индекс факт.адреса
    def check_org_index_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(3)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_INDEX
        if value == user_constants.USER_ORG_INDEX:
            print('Индекс факт.адреса корректный')

    # пользователь вносит улицу
    def user_fill_org_street(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(3)>form>div>div:nth-child(4)>div>div>div.el-input>input'),
                           user_constants.USER_ORG_STREET)

    # пользователь проверяет улицу юр.адреса
    def check_org_street_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(4)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_STREET
        if value == user_constants.USER_ORG_STREET:
            print('Улица юр.адреса корректная')

    # пользователь проверяет улицу факт.адреса
    def check_org_street_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(4)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_STREET
        if value == user_constants.USER_ORG_STREET:
            print('Улица факт.адреса корректная')

    # пользователь вносит номер дома
    def user_fill_org_house(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(3)>form>div>div:nth-child(5)>div>div>div>input'),
                           user_constants.USER_ORG_HOUSE)

    # пользователь проверяет номер дома юр.адреса
    def check_org_house_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(5)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_HOUSE
        if value == user_constants.USER_ORG_HOUSE:
            print('Номер дома юр.адреса корректный')

    # пользователь проверяет номер дома факт.адреса
    def check_org_house_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(5)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_HOUSE
        if value == user_constants.USER_ORG_HOUSE:
            print('Номер дома факт.адреса корректный')

    # пользователь вносит офис
    def user_fill_org_office(self):
        BasePage.send_keys(self,
                           (By.CSS_SELECTOR,
                            'div.organization>div:nth-child(3)>form>div>div:nth-child(6)>div>div>div.el-input>input'),
                           user_constants.USER_ORG_OFFICE)

    # пользователь проверяет номер офиса юр.адреса
    def check_org_office_legal(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(3)>div>div:nth-child(6)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_OFFICE
        if value == user_constants.USER_ORG_OFFICE:
            print('Номер офиса юр.адреса корректный')

    # пользователь проверяет номер офиса факт.адреса
    def check_org_office_actual(self):
        value = BasePage.get_text(self,
                                  (By.CSS_SELECTOR,
                                   'div.organization>div:nth-child(4)>div>div:nth-child(6)>p.organization-info__value'))
        assert value == user_constants.USER_ORG_OFFICE
        if value == user_constants.USER_ORG_OFFICE:
            print('Номер офиса факт.адреса корректный')

    # пользователь отмечает, что юридический и фактический адреса совпадают
    def click_checkbox_org_same_address(self):
        BasePage.click(self, (By.CSS_SELECTOR, '[class="el-switch__core"]'))

    # пользователь нажимает чекбокс с текстом
    # Нажимая "Сохранить данные" я даю согласие на обработку персональных данных
    def click_checkbox_edit_org_save_data(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR, '[class="el-checkbox__inner"]'))

    # пользователь нажимает кнопку "Сохранить данные"
    def click_btn_send_data(self):
        BasePage.click(self,
                       (By.CSS_SELECTOR,
                        'div.organization > button > span'))

    # проверяем, что появляется сообщение "данные успешно сохранены"
    def check_request_edit_org_accepted(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR, 'div > div > div.el-notification__content'))
        assert text == 'Данные организации сохранены!'
        if text == 'Данные организации сохранены!':
            print("Пользователь видит сообщение об успешном сохранен данных организации")

    # прокрутка страницы вверх
    def page_up(self):
        element = self.driver.find_element_by_css_selector(
            'div.organization>div:nth-child(1)>form>div>div:nth-child(4)>div>div>div.el-input>input')
        element.send_keys(Keys.CONTROL + Keys.HOME)
