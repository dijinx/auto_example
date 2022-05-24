from pages.Favorites import Favorites
import pytest
import allure
import time

# для теста у пользователя должна быть пустая корзина
@allure.suite('Smoke')
@allure.title('Пользователь успешно добавляет объект в корзину')
@allure.description('Пользователь успешно добавляет объект в корзину')
@pytest.mark.run(order=4)
@pytest.mark.smoke
@pytest.mark.user
def test_add_to_bucket_from_favorites(driver):
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
    with allure.step('Пользователь нажимает кнопку "Добавить в корзину"'):
        favorites.add_to_bucket()
    with allure.step('Пользователь открывает корзину'):
        favorites.click_on_bucket()
    with allure.step('Пользователь проверяет объект в корзине'):
        favorites.get_bucket_object_text()
    with allure.step('Пользователь удаляет объект из корзины'):
        favorites.delete_from_bucket()
