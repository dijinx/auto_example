import time
import pytest
import allure
from pages.Favorites import Favorites
from pages.ModerTaskPage import ModerTaskPage


@allure.suite('Smoke')
@allure.title('Пользователь создаёт запрос')
@allure.description('Пользователь создаёт запрос')
@pytest.mark.run(order=9)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_user(driver):
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор успешно выставляет запросу статус "Есть в перечне", докам статус "Нет ошибок"')
@allure.description('Модератор успешно выставляет запросу статус "Есть в перечне", докам статус "Нет ошибок"')
@pytest.mark.run(order=9)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_moder(driver):
    moder = ModerTaskPage(driver)

    # модератор проверяет ставит есть в перечне, проверяет доки в статус "есть ошибки",
    # отправляет пользователю шаблон письма №1
    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор открывает страницу "Задачи"'):
        moder.open_moder_page()
    with allure.step('Модератор нажимает карточку заказа'):
        moder.click_on_request_card()
        time.sleep(2)
    with allure.step('Модератор нажимает кнопку "Взять в работу"'):
        moder.click_btn_take_to_work()
    with allure.step('Модератор нажимает радиоботтон "Есть в перечне"'):
        moder.click_btn_is_in_scroll()
    with allure.step('Модератор нажимает по выпадающему списку статуса для рыночного отчёта'):
        moder.click_market_price_report_status_menu()
    with allure.step('Модератор выставляет рыночному отчёту статус "Нет ошибок"'):
        moder.click_no_errors_in_market_price_report()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса рыночного отчёта'):
        moder.click_btn_save_market_price_status()
        time.sleep(2)
    with allure.step('Модератор нажимает по выпадающему списку статуса для ЭЦП1'):
        moder.click_ecp_1_status_menu()
    with allure.step('Модератор выставляет ЭЦП1 статус "Нет ошибок"'):
        moder.click_no_errors_in_ecp_1()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП1'):
        moder.click_btn_save_ecp_1_status()
        time.sleep(2)
    with allure.step('Модератор нажимает по выпадающему списку статуса для ЭЦП2'):
        moder.click_ecp_2_status_menu()
    with allure.step('Модератор выставляет ЭЦП2 статус "Нет ошибок"'):
        moder.click_no_errors_in_ecp_2()
    with allure.step('Модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП2'):
        moder.click_btn_save_ecp_2_status()
    with allure.step('Модератор загружает выписку из ЕГРН'):
        moder.load_extract_from_egrn_file()
        time.sleep(3)
    with allure.step('Модератор загружает ЭЦП к выписке из ЕГРН'):
        moder.load_ecp_for_extract_from_egrn()
    with allure.step('Модератор нажимает на слово "здесь" в надписи Впишите данные рыночного отчета здесь'):
        moder.click_word_here_in_inscription()
    with allure.step('Модератор вносит стоимость объекта в модальном окне'):
        moder.insert_market_price_value_in_modal_market_report()
    with allure.step('Модератор вносит номер отчёта в модальном окне'):
        moder.insert_number_of_market_report_in_modal_market_report()
    with allure.step('Модератор выставляет дату для отчёта в модальном окне'):
        moder.insert_date_market_report_in_modal_market_report()
    with allure.step('Модератор нажимает кнопку "Сохранить в модальном окне"'):
        moder.click_btn_save_in_modal_market_report()
    with allure.step('Модератор выбирает форму ответа для отправки пользователю'):
        moder.select_letter_for_user_pattern_num_1()
    with allure.step('Модератор нажимает кнопку "Отправить результат"'):
        moder.send_result_to_user()
        time.sleep(2)
    with allure.step('Модератор проверяет, что результат проверки отправлен пользователю'):
        moder.check_result_is_send_to_user()
