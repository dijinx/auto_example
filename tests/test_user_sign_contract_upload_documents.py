import time

import pytest
import allure

from pages.OrderPage import OrderPage
from pages.RequestOrdersPage import RequestOrdersPage
from pages.StartPage import StartPage
from pages.UserProfilePage import UserProfilePage


# для генерации данных для теста запустить тест ордер = 9
@allure.suite('Smoke')
@allure.title('Пользователь успешно подписывает договор на основные услуги и договор на суд.представительство')
@allure.description('Пользователь успешно подписывает договор на основные услуги и договор на суд.представительство')
@pytest.mark.run(order=10)
@pytest.mark.smoke
@pytest.mark.user
def test_user_sign_contract(driver):
    start_page = StartPage(driver)
    request_orders = RequestOrdersPage(driver)
    order = OrderPage(driver)

    with allure.step('Пользователь авторизуется'):
        start_page.login()
        time.sleep(3)
    with allure.step('Пользователь открывает страницу с заказами'):
        request_orders.open_request_orders()
    with allure.step('Пользователь нажимает на карточку заказа'):
        request_orders.click_on_request_card_btn_continue()
    with allure.step('Пользователь нажимает кнопку "Следующий шаг"'):
        order.click_btn_next_step()
    with allure.step('Пользователь нажимает чекбокс "Судебное представительство"'):
        order.click_checkbox_in_judicial_representation()
        time.sleep(2)
    with allure.step('Пользователь нажимает кнопку "Следующий шаг"'):
        order.click_btn_next_step()
        time.sleep(3)
    # with allure.step('Пользователь переходит к заполнению своих данных'):TODO закомментировал для пробы
    #     order.click_btn_go_over()
    # with allure.step('Пользователь нажимает по ссылке в пуше "перейти к заказу"'):
    #     order.click_push_data_successfully_filled()
    with allure.step('Пользователь вносит ФИО для договора'):
        order.enter_user_fio()
    with allure.step('Пользователь вносит должность для договора'):
        order.enter_user_position()
    with allure.step('Пользователь вносит имя документа подтверждения'):
        order.enter_user_document_name()
    with allure.step('Пользователь нажимает кнопку "Данные договоров совпадают"'):
        order.click_checkbox_contract_data_are_same()
    with allure.step('Пользователь нажимает чекбокс "Принимаю и подтверждаю"'):
        order.click_checkbox_confirm_and_agree()
        time.sleep(7)
    with allure.step('Пользователь нажимает кнопку "Подписать договор и получить счёт"'):
        order.click_btn_continue_and_get_check()
        time.sleep(15)
    with allure.step('Пользователь проверяет, что запрос отправлен'):
        order.check_request_is_send()


@allure.suite('Smoke')
@allure.title('Пользователь успешно загружает документы и отправляет их')
@allure.description('Пользователь успешно загружает документы и отправляет их')
@pytest.mark.run(order=10)
@pytest.mark.smoke
@pytest.mark.user
def test_user_upload_documents(driver):
    start_page = StartPage(driver)
    request_orders = RequestOrdersPage(driver)
    order = OrderPage(driver)
    profile = UserProfilePage(driver)

    with allure.step('Пользователь авторизуется'):
        start_page.login()
        time.sleep(3)
    with allure.step('Пользователь открывает страницу "Мои запросы"'):
        request_orders.open_request_orders()
    with allure.step('Пользователь нажимает на карточку заказа'):
        request_orders.click_on_request_card_btn_continue()
        time.sleep(3)
    # with allure.step('Пользователь нажимает пуш-уведомление "Заполнить данные"'): TODO закомментировал для пробы
    #     order.click_btn_fill_data()
    #     time.sleep(5)
    # with allure.step('Пользователь нажимает чекбокс "Сохранить данные"'):
    #     profile.click_checkbox_save_data()
    #     time.sleep(2)
    # with allure.step('Пользователь нажимает кнопку "Сохранить данные"'):
    #     profile.click_btn_save_data()
    with allure.step('Пользователь открывает страницу заказов'):
        request_orders.open_request_orders()
    with allure.step('Пользователь нажимает карточку заказа'):
        request_orders.click_on_request_card_btn_continue()
        time.sleep(4)
    with allure.step('Пользователь загружает правоустанавливающий документ на объект'):
        order.load_establishing_document_on_object()
    with allure.step('Пользователь загружает заявление в комиссию'):
        order.load_statement_to_the_commission()
        time.sleep(2)
    with allure.step('Пользователь загружает ЭЦП к заявлению в комиссию'):
        order.load_ecp_for_statement_to_the_commission()
    with allure.step('Пользователь загружает решение комиссии'):
        order.load_decision_of_the_commission()
    with allure.step('Пользователь нажимает кнопку "Следующий шаг"'):
        order.click_btn_next_step()
        time.sleep(20)
    with allure.step('Пользователь проверяет, что запрос отправлен'):
        order.check_request_successfully_accepted()
