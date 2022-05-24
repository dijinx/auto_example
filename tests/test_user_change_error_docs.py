import time

import pytest
import allure

from pages.OrderPage import OrderPage
from pages.RequestOrdersPage import RequestOrdersPage
from pages.StartPage import StartPage


@allure.suite('Smoke')
@allure.title('Пользователь успешно заменяет документы')
@allure.description('Пользователь успешно заменяет документы')
@pytest.mark.run(order=8)
@pytest.mark.smoke
@pytest.mark.user
def test_user_change_error_docs(driver):
    start_page = StartPage(driver)
    request_orders = RequestOrdersPage(driver)
    order = OrderPage(driver)

    with allure.step('Пользователь авторизуется'):
        start_page.login()
        time.sleep(3)
    with allure.step('Пользователь открывает карточку заказа'):
        request_orders.open_request_orders()
    with allure.step('Пользователь нажимает кнопку "Продолжить заказ" на карточке заказа'):
        request_orders.click_on_request_card_btn_continue()
    with allure.step('Пользователь удаляет рыночный отчёт'):
        order.delete_document()
    with allure.step('Пользователь удаляет ЭЦП1'):
        order.delete_document()
    with allure.step('Пользователь удаляет ЭЦП2'):
        order.delete_document()
        time.sleep(2)
    with allure.step('Пользователь загружает новый рыночный отчёт'):
        order.load_market_prise_report()
        time.sleep(2)
    with allure.step('Пользователь загружает новую ЭЦП1'):
        order.load_ecp_1()
    with allure.step('Пользователь загружает новую ЭЦП2'):
        order.load_ecp_2()
    with allure.step('Пользователь проверяет, что ЭЦП1 загружена'):
        order.check_ecp_1_is_load()
    with allure.step('Пользователь проверяет, что рыночный отчёт загружен'):
        order.check_market_report_is_load()
    with allure.step('Пользователь проверяет, что ЭЦП2 загружена'):
        order.check_ecp_2_is_load()
    with allure.step('Пользователь нажимает кнопку "Следующий шаг"'):
        order.click_btn_next_step()
    with allure.step('Пользователь проверяет что запрос отправлен'):
        order.check_request_is_accepted()
