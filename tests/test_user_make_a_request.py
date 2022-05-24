import time
import pytest
import allure
from pages.Favorites import Favorites
from pages.OrderPage import OrderPage


@allure.suite('Smoke')
@allure.title('Пользователь успешно создает запрос')
@allure.description('Пользователь успешно создает запрос')
@pytest.mark.run(order=5)
@pytest.mark.smoke
@pytest.mark.user
def test_make_a_request(driver):
    favorites = Favorites(driver)
    order = OrderPage(driver)

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
    with allure.step('Пользователь нажимает на корзину'):
        favorites.click_on_bucket()
    with allure.step('Пользователь нажимает кнопку "Составить запрос"'):
        favorites.click_btn_make_request()
    with allure.step('Пользователь загружает рыночный отчёт'):
        order.load_market_prise_report()
        time.sleep(2)
    with allure.step('Пользователь загружает ЭЦП1'):
        order.load_ecp_1()
    with allure.step('Пользователь загружает ЭЦП2'):
        order.load_ecp_2()
    with allure.step('Пользователь проверяет, что рыночный отчёт загружен'):
        order.check_market_report_is_load()
    with allure.step('Пользователь проверяет, что ЭЦП1 загружена'):
        order.check_ecp_1_is_load()
    with allure.step('Пользователь проверяет, что ЭЦП2 загружена'):
        order.check_ecp_2_is_load()
    with allure.step('Пользователь нажимает кнопку "Следующий шаг"'):
        order.click_btn_next_step()
    with allure.step('Пользователь проверяет, что запрос отправлен'):
        order.check_request_is_accepted()
