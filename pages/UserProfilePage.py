from constants import user_constants
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class UserProfilePage(BasePage):

    # пользователь открывает страницу "Мой профиль"
    def open_profile_user(self):
        BasePage.open_site(self, user_constants.USER_PROD_MY_PROFILE_PAGE)

    # авторизация нового пользователя
    def new_user_auth(self):
        BasePage.user_auth_new_user_for_profile_and_requisites(self)

    # пользователь проверяет ссылку страницы, должна быть https://estate.mts.ru/profile/user
    def check_url_is_profile_user(self):
        url = BasePage.get_url(self)
        assert url == user_constants.USER_PROD_MY_PROFILE_PAGE
        if url == user_constants.USER_PROD_MY_PROFILE_PAGE:
            print('URL верный.')

    # пользователь вносит фамилию
    def user_fill_last_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Иванов"]'), user_constants.USER_LAST_NAME)

    # пользователь проверяет фамилию
    def user_check_last_name_in_profile(self):
        value = self.driver.execute_script(
            'return document.querySelector("#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.grid.grid_cols_3.grid_cols_m_2.grid_cols_xs_1 > div:nth-child(1) > div > div > div > input").value')
        assert value == user_constants.USER_LAST_NAME
        if value == user_constants.USER_LAST_NAME:
            print('Ожидаемая фамилия: ' + user_constants.USER_LAST_NAME + '\n' + 'Фамилия в профиле: ' + value)

    # пользователь вносит имя
    def user_fill_first_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Иван"]'), user_constants.USER_FIRST_NAME)

    # пользователь проверяет имя
    def user_check_first_name(self):
        value = self.driver.execute_script(
            'return document.querySelector("#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.grid.grid_cols_3.grid_cols_m_2.grid_cols_xs_1 > div:nth-child(2) > div > div > div.el-input > input").value')
        assert value == user_constants.USER_FIRST_NAME
        if value == user_constants.USER_FIRST_NAME:
            print('Ожидаемое имя: ' + user_constants.USER_FIRST_NAME + '\n' + 'Имя в профиле: ' + value)

    # пользователь вносит отчество
    def user_fill_second_name(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="Иванович"]'), user_constants.USER_SECOND_NAME)

    # пользователь проверяет отчество
    def user_check_second_name(self):
        value = self.driver.execute_script(
            'return document.querySelector("#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.grid.grid_cols_3.grid_cols_m_2.grid_cols_xs_1 > div:nth-child(3) > div > div > div.el-input > input").value')
        assert value == user_constants.USER_SECOND_NAME
        if value == user_constants.USER_SECOND_NAME:
            print('Ожидаемое отчество: ' + user_constants.USER_SECOND_NAME + '\n' + 'Отчество в профиле: ' + value)

    # пользователь вносит дату рождения
    def user_fill_birth_date(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="01.01.1990"]'), user_constants.USER_BIRTH_DATE)

    # пользователь проверяет дату рождения
    def user_check_birth_date(self):
        value = self.driver.execute_script(
            'return document.querySelector("#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.grid.grid_cols_3.grid_cols_m_2.grid_cols_xs_1 > div:nth-child(4) > div > div > div.el-date-editor.form-customer-user__date-picker.el-input.el-input--prefix.el-input--suffix.el-date-editor--date > input").value')
        assert value == user_constants.USER_BIRTH_DATE
        if value == user_constants.USER_BIRTH_DATE:
            print(
                'Ожидаемая дата: ' + user_constants.USER_BIRTH_DATE + '\n' + 'Дата в профиле: ' + value)

    # пользователь вносит электронную почту
    def user_fill_email(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="example@test.ru"]'), user_constants.USER_MAIL)

    # пользователь проверяет  электронную почту
    def user_check_email(self):
        value = self.driver.execute_script(
            'return document.querySelector("#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.grid.grid_cols_3.grid_cols_m_2.grid_cols_xs_1 > div:nth-child(5) > div > div > div.el-input > input").value')
        assert value == user_constants.USER_MAIL
        if value == user_constants.USER_MAIL:
            print(
                'Ожидаемая почта: ' + user_constants.USER_MAIL + '\n' + 'Почта в профиле: ' + value)

    # пользователь вносит свой адрес
    def user_fill_address(self):
        BasePage.send_keys(self, (
            By.XPATH, '//*[@placeholder="Московская область, г. Москва, ул. Ковальчука, д. 12, кв. 1"]'),
                           user_constants.USER_ADDRESS)

    # пользователь проверяет адрес
    def user_check_address(self):
        value = self.driver.execute_script(
            "return document.querySelector('#app > div.page > div > div.page-container > div > div > main > main > div > form > div > div.el-form-item.is-success.is-required > div > div > input').value")
        assert value == user_constants.USER_ADDRESS
        if value == user_constants.USER_ADDRESS:
            print(
                'Ожидаемый адрес: ' + user_constants.USER_ADDRESS + '\n' + 'Адрес в профиле: ' + value)

    # пользователь нажимает чекбокс с текстом
    # "Нажимая "Сохранить данные" я даю согласие на обработку персональных данных"
    def click_checkbox_save_data(self):
        BasePage.click(self, (By.XPATH, '//*[@class="el-checkbox__inner"]'))

    # пользователь нажимает кнопку "Сохранить данные"
    def click_btn_save_data(self):
        BasePage.click(self, (By.XPATH, '//*[1][@class="el-button el-button--primary el-button--small"]'))
