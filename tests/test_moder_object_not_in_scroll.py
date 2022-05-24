from pages.Favorites import Favorites
from pages.ModerTaskPage import ModerTaskPage
from pages.StartPage import StartPage
import time
import allure
import pytest
from pages.RequestOrdersPage import RequestOrdersPage


@allure.suite('Smoke')
@allure.title('Пользователь создаёт заказ')
@allure.description('Пользователь создаёт заказ')
@pytest.mark.run(order=6)
@pytest.mark.smoke
@pytest.mark.moder
def test_mod_object_not_in_scroll(driver):
    favorites = Favorites(driver)

    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор успешно выставляет запросу статус "Нет в перечне"')
@allure.description('Модератор успешно выставляет запросу статус "Нет в перечне"')
@pytest.mark.run(order=6)
@pytest.mark.smoke
@pytest.mark.moder
def test_mod_object_not_in_scroll_moder(driver):
    moder = ModerTaskPage(driver)

    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор открывает страницу "Задачи"'):
        moder.open_moder_page()
    with allure.step('Модератор нажимает карточку заказа'):
        moder.click_on_request_card()
        time.sleep(5)
    with allure.step('Модератор нажимает кнопку "Взять в работу"'):
        moder.click_btn_take_to_work()
    with allure.step('Модератор нажимает радиоботтон "Нет в перечне"'):
        moder.click_btn_not_in_scroll()
    with allure.step('Модератор выбирает форму ответа пользователю'):
        moder.select_letter_for_user_pattern_num_1()
    with allure.step('Модератор отправляет результат проверки пользователю'):
        moder.send_result_to_user()


@allure.suite('Smoke')
@allure.title('Пользователь проверяет статус заказа. Статус "Заказ отменён"')
@allure.description('Пользователь проверяет статус заказа. Статус "Заказ отменён"')
@pytest.mark.run(order=6)
@pytest.mark.smoke
@pytest.mark.moder
def test_mod_object_not_in_scroll_user(driver):
    start_page = StartPage(driver)
    order_request = RequestOrdersPage(driver)
    # пользователь
    with allure.step('Пользователь авторизуется'):
        start_page.login()
        time.sleep(3)
    with allure.step('Пользователь открывает страницу заказов'):
        order_request.open_request_orders()
        time.sleep(3)
    with allure.step('Пользователь выбирает карточку заказа'):
        order_request.click_on_request_card()
        time.sleep(3)
    with allure.step('Пользователь проверяет статус заказа. Статус заказа "Заказ отменён"'):
        order_request.check_request_status_is_denied()
