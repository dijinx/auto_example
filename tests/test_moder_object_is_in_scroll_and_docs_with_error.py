import time
import pytest
import allure
from pages.Favorites import Favorites
from pages.ModerTaskPage import ModerTaskPage


@allure.suite('Smoke')
@allure.title('Модератор успешно выставляет запросу статус "Есть в перечне", докам статус "Есть ошибки"')
@allure.description('Модератор успешно выставляет запросу статус "Есть в перечне", докам статус "Есть ошибки"')
@pytest.mark.run(order=7)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll(driver):
    moder = ModerTaskPage(driver)
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()
    # модератор проверяет ставит есть в перечне, проверяет доки в статус "есть ошибки",
    # отправляет пользователю шаблон №1
    with allure.step('Модератор открывает страницу "Задачи"'):
        moder.open_moder_page()
    with allure.step('Модератор нажимает на карточку заказа'):
        moder.click_on_request_card()
        time.sleep(2)
    with allure.step('Модератор нажимает кнопку "Взять в работу"'):
        moder.click_btn_take_to_work()
    with allure.step('Модератор нажимает радиоботтон "Есть в перечне"'):
        moder.click_btn_is_in_scroll()
    with allure.step('Модератор нажимает на меню выставления статуса для рыночного отчёта'):
        moder.click_market_price_report_status_menu()
    with allure.step('Модератор выставляет рыночному отчёту статус "Есть ошибки"'):
        moder.click_have_errors_in_market_price_report()
    with allure.step('Модератор вносит текст в окно описания ошибки для рыночного отчёта'):
        moder.enter_text_in_error_textarea_market_price()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса рыночного отчёта'):
        moder.click_btn_save_market_price_status()
        time.sleep(2)
    with allure.step('Модератор нажимает на меню выставления статуса для ЭЦП1'):
        moder.click_ecp_1_status_menu()
    with allure.step('Модератор выставляет ЭЦП1 статус "Есть ошибки"'):
        moder.click_have_errors_in_ecp_1()
    with allure.step('Модератор вносит текст в окно описания ошибки для ЭЦП1'):
        moder.enter_text_in_error_textarea_ecp_1()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП1'):
        moder.click_btn_save_ecp_1_status()
        time.sleep(2)
    with allure.step('Модератор нажимает на меню выставления статуса для ЭЦП1'):
        moder.click_ecp_2_status_menu()
    with allure.step('Модератор выставляет ЭЦП1 статус "Есть ошибки"'):
        moder.click_have_errors_in_ecp_2()
    with allure.step('Модератор вносит текст в окно описания ошибки для ЭЦП1'):
        moder.enter_text_in_error_textarea_ecp_2()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП1'):
        moder.click_btn_save_ecp_2_status()
    with allure.step('Модератор загружает выписку из ЕГРН'):
        moder.load_extract_from_egrn_file()
        time.sleep(3)
    with allure.step('Модератор загружает ЭЦП к выписке из ЕГРН'):
        moder.load_ecp_for_extract_from_egrn()
    with allure.step('Модератор выбирает форму ответа для отправки модератору'):
        moder.select_letter_for_user_pattern_num_1()
    with allure.step('Модератор нажимает кнопку "Отправить результат"'):
        moder.send_result_to_user()
        time.sleep(2)
    with allure.step('Модератор проверяет, что результат отправлен пользователю'):
        moder.check_result_is_send_to_user()
