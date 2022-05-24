from pages.Favorites import Favorites
import pytest
import allure
import time


@allure.suite('Smoke')
@allure.title('Пользователь успешно осуществляет поиск по кадастровому номеру')
@allure.description('Пользователь успешно осуществляет поиск по кадастровому номеру')
@pytest.mark.run(order=2)
@pytest.mark.smoke
@pytest.mark.user
def test_search_cadastral_number(driver):
    favorites = Favorites(driver)

    with allure.step('Пользователь авторизуется'):
        favorites.login()
        time.sleep(3)
    with allure.step('Пользователь открывает страницу "Мои объекты"'):
        favorites.open_favorites()
    with allure.step('Пользователь вносит кадастровый номер'):
        favorites.enter_cadastral_number()
    with allure.step('Пользователь нажимает кнопку "Найти"'):
        favorites.click_btn_search_object()
    with allure.step('Пользователь проверяет, что объект найден'):
        favorites.check_address()
