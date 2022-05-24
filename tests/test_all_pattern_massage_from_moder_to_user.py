import pytest
import allure
import time

from pages.Favorites import Favorites
from pages.ModerTaskPage import ModerTaskPage
from pages.UserEmailPage import UserEmailPage


@allure.suite('Smoke')
@allure.title('Подготовка, пользователь создаёт запрос для шаблона №1')
@allure.description('Подготовка, пользователь создаёт запрос для шаблона №1')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_user_create_request(driver):
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №1')
@allure.description('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №1')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_moder_with_1_pattern(driver):
    moder = ModerTaskPage(driver)

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
    with allure.step('Модератор нажимает радиоботтон "Нет в перечне"'):
        moder.click_btn_not_in_scroll()
    with allure.step('Модератор выбирает форму ответа пользователю №1'):
        moder.select_letter_for_user_pattern_num_1()
    with allure.step('Модератор вносит текст в поле шаблона ответа пользователю'):
        moder.enter_pattern_1_text()
    with allure.step('Модератор отправляет результат проверки пользователю'):
        moder.send_result_to_user()


# пользователь заходит в ящик и проверяет наличие письма с текстом шаблона №1
@allure.suite('Smoke')
@allure.title('Пользователь проверяет почтовый ящик на наличие шаблона письма №1')
@allure.description('Пользователь проверяет почтовый ящик на наличие шаблона письма №1')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_pattern_massage_num_1_from_moder_to_user(driver):
    user = UserEmailPage(driver)

    with allure.step('пользователь авторизуется в почтовом ящике'):
        user.open_email_site_and_authorize()
        time.sleep(5)
    with allure.step('пользователь выбирает письмо шаблон 1'):
        user.user_select_letter_pattern_1_in_email_box()
    with allure.step('пользователь проверяет текст письма'):
        user.check_letter_pattern_1_in_email_box()


# пользователь создает заказ - отправляет модератору 2
@allure.suite('Smoke')
@allure.title('Подготовка, пользователь создаёт запрос для шаблона №2')
@allure.description('Подготовка, пользователь создаёт запрос для шаблона №2')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_user_create_request_2(driver):
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №2')
@allure.description('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №2')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_moder_with_2_pattern(driver):
    moder = ModerTaskPage(driver)

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
    with allure.step('Модератор нажимает радиоботтон "Нет в перечне"'):
        moder.click_btn_not_in_scroll()
    with allure.step('Модератор выбирает форму №2 ответа пользователю'):
        moder.select_letter_for_user_pattern_num_2()
    with allure.step('Модератор вносит текст в поле шаблона ответа пользователю'):
        moder.enter_pattern_2_text()
    with allure.step('Модератор отправляет результат проверки пользователю'):
        moder.send_result_to_user()
        moder.insert_date_market_report_in_modal_market_report()


# пользователь заходит в ящик и проверяет наличие письма с текстом шаблона №2
@allure.suite('Smoke')
@allure.title('Пользователь проверяет почтовый ящик на наличие шаблона письма №2')
@allure.description('Пользователь проверяет почтовый ящик на наличие шаблона письма №2')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_pattern_massage_num_2_from_moder_to_user(driver):
    user = UserEmailPage(driver)

    with allure.step('Пользователь авторизуется в почтовом ящике'):
        user.open_email_site_and_authorize()
        time.sleep(5)
    with allure.step('Пользователь выбирает письмо шаблон 2'):
        user.user_select_letter_pattern_2_in_email_box()
    with allure.step('Пользователь проверяет текст письма'):
        user.check_letter_pattern_2_in_email_box()


# пользователь создает заказ - отправляет модератору 3
@allure.suite('Smoke')
@allure.title('Подготовка, пользователь создаёт запрос для шаблона письма №3')
@allure.description('Подготовка, пользователь создаёт запрос для шаблона письма №3')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_user_create_request_3(driver):
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №3')
@allure.description('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №3')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_moder_with_3_pattern(driver):
    moder = ModerTaskPage(driver)

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
    with allure.step('Модератор нажимает радиоботтон "Нет в перечне"'):
        moder.click_btn_not_in_scroll()
    with allure.step('Модератор выбирает форму №3 ответа пользователю'):
        moder.select_letter_for_user_pattern_num_3()
    with allure.step('Модератор вносит текст в поле шаблона ответа пользователю'):
        moder.enter_pattern_3_text()
    with allure.step('Модератор отправляет результат проверки пользователю'):
        moder.send_result_to_user()


# пользователь заходит в ящик и проверяет наличие письма с текстом шаблона 3
@allure.suite('Smoke')
@allure.title('Пользователь проверяет почтовый ящик на наличие шаблона письма №3')
@allure.description('Пользователь проверяет почтовый ящик на наличие шаблона письма №3')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_pattern_massage_num_3_from_moder_to_user(driver):
    user = UserEmailPage(driver)

    with allure.step('Пользователь авторизуется в почтовом ящике'):
        user.open_email_site_and_authorize()
        time.sleep(5)
    with allure.step('Пользователь выбирает письмо шаблон 3'):
        user.user_select_letter_pattern_3_in_email_box()
    with allure.step('Пользователь проверяет текст письма'):
        user.check_letter_pattern_3_in_email_box()


# пользователь создает заказ - отправляет модератору 4
@allure.suite('Smoke')
@allure.title('Подготовка, пользователь создаёт запрос')
@allure.description('Подготовка, пользователь создаёт запрос')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_user_create_request_4(driver):
    favorites = Favorites(driver)

    # пользователь создаёт запрос
    favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №4')
@allure.description('Модератор обрабатывает запрос и отправляет пользователю шаблон письма №4')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_object_is_in_scroll_moder_with_4_pattern(driver):
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
    with allure.step('Модератор выбирает форму №4 ответа пользователю'):
        moder.select_letter_for_user_pattern_num_4()
    with allure.step('Модератор вносит текст в поле шаблона ответа пользователю'):
        moder.enter_pattern_4_text()
    with allure.step('Модератор отправляет результат проверки пользователю'):
        moder.send_result_to_user()


# пользователь заходит в ящик и проверяет наличие письма с текстом шаблона №4
@allure.suite('Smoke')
@allure.title('Пользователь проверяет почтовый ящик на наличие шаблона письма №4')
@allure.description('Пользователь проверяет почтовый ящик на наличие шаблона письма №4')
@pytest.mark.run(order=15)
@pytest.mark.smoke
@pytest.mark.user
def test_pattern_massage_num_4_from_moder_to_user(driver):
    user = UserEmailPage(driver)

    with allure.step('Пользователь авторизуется в почтовом ящике'):
        user.open_email_site_and_authorize()
        time.sleep(5)
    with allure.step('Пользователь выбирает письмо шаблон 4'):
        user.user_select_letter_pattern_4_in_email_box()
    with allure.step('Пользователь проверяет текст письма'):
        user.check_letter_pattern_4_in_email_box()
