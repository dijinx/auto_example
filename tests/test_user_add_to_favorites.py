from pages.Favorites import Favorites
import pytest
import allure
import time

# для теста искомый объект должен отсутствовать в избранном у пользователя
@allure.suite('Smoke')
@allure.title('Пользователь успешно добавляет объект в избранное')
@allure.description('Пользователь успешно добавляет объект в избранное')
@pytest.mark.run(order=3)
@pytest.mark.smoke
@pytest.mark.user
def test_add_to_favorites(driver):
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
    with allure.step('Пользователь добавляет объект в избранное'):
        favorites.add_to_favorites()
    with allure.step('Пользователь проверяет объект в избранном'):
        favorites.check_object_in_favorites()
    with allure.step('Пользователь удаляет объект из избранного'):
        favorites.delete_from_favorites()
