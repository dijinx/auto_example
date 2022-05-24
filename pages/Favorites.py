import time

from selenium.webdriver.common.by import By

from constants import user_constants
from pages.BasePage import BasePage


class Favorites(BasePage):

    # пользователь создаёт заказ
    def user_create_request(self):
        BasePage.user_create_request(self)

    # пользователь авторизуется
    def login(self):
        BasePage.user_auth(self)

    # пользователь открывает страницу "Мои объекты"
    def open_favorites(self):
        BasePage.open_site(self, user_constants.USER_PROD_FAVORITES_PAGE)

    # пользователь вводит кадастровый номер
    def enter_cadastral_number(self):
        BasePage.send_keys(self, (By.ID, 'search-input'), user_constants.USER_CADASTRAL_NUMBER_0)

    # пользователь нажимает кнопку "Найти объект"
    def click_btn_search_object(self):
        BasePage.click(self, (By.ID, 'search-btn'))
        time.sleep(5)

    # пользователь проверяет сохранённый в профиле адрес
    def check_address(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="search__address"]'))
        assert text == user_constants.USER_CADASTRAL_NUMBER_0_ADDRESS

    # пользователь добавляет объект в избранное
    def add_to_favorites(self):
        BasePage.click(self, (By.XPATH, '//*[@data-test-id="favorite-button"]'))

    # пользователь проверяет объект в избранном после его добавления
    # данные в методе предназначены для конкретного объекта 77:01:0004015:1020
    # при изменении кадастрового номера необходимо заменить адрес
    def check_object_in_favorites(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@id="search-section"]/div/div[3]/div/div[1]/h4'))
        assert text == 'Россия, Москва, Лесная улица, 10-16'
        print("Верный объект")

    # пользователь удаляет объект из избранного
    def delete_from_favorites(self):
        BasePage.click(self, (By.XPATH, '//*[@data-test-id="favorite-button"]'))

    # пользователь добавляет объект в корзину
    def add_to_bucket(self):
        BasePage.click(self, (By.XPATH, '//*[@data-test-id="add-to-cart-button"]'))

    # пользователь кликает по иконке корзины
    def click_on_bucket(self):
        BasePage.click(self, (By.XPATH, '//*[@class="profile-widget-cart"]'))

    # пользователь проверяет - верный ли объект находится в корзине
    def get_bucket_object_text(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="cart-item__title"]'))
        assert text == user_constants.USER_CADASTRAL_NUMBER_0
        if text == user_constants.USER_CADASTRAL_NUMBER_0:
            print("В корзине верный объект")
        time.sleep(5)

    # пользователь удаляет объект из корзины
    def delete_from_bucket(self):
        BasePage.click(self, (By.XPATH, '//*[@class="cart-item__close"]'))

    # пользователь нажимает кнопку "Составить запрос"
    def click_btn_make_request(self):
        BasePage.click(self,
                       (By.XPATH, '//*[@class="el-button cart__actions-btn el-button--primary el-button--small"]'))
