import time

import pytest
import allure

from pages.Favorites import Favorites
from pages.ModerTaskPage import ModerTaskPage


@allure.suite('Smoke')
@allure.title('Подготовка: пользователь создаёт заказ')
@allure.description('Подготовка: пользователь создаёт заказ')
@pytest.mark.run(order=13)
@pytest.mark.smoke
@pytest.mark.moder
def test_user_create_request(driver):
    favorites = Favorites(driver)

    with allure.step('Пользователь создаёт заказ'):
        favorites.user_create_request()


@allure.suite('Smoke')
@allure.title('Модератор проверяет отображение реквизитов компании пользователя в заказе')
@allure.description('Модератор проверяет отображение реквизитов компании пользователя в заказе')
@pytest.mark.run(order=13)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_check_organization_data_in_request(driver):
    moder = ModerTaskPage(driver)

    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор переходит на страницу задачи'):
        moder.open_moder_page()
    with allure.step('Модератор открывает задачу'):
        moder.click_on_request_card()
        time.sleep(5)
    with allure.step('Модератор проверяет тип владения'):
        moder.moder_check_type_of_ownership()
    with allure.step('Модератор проверяет юридическое наименование'):
        moder.moder_check_legal_name()
    with allure.step('Модератор проверяет ИНН'):
        moder.moder_check_inn()
    with allure.step('Модератор проверяет КПП'):
        moder.moder_check_kpp()
    with allure.step('Модератор проверяет ОКТМО'):
        moder.moder_check_oktmo()
    with allure.step('Модератор проверяет ОКАТО'):
        moder.moder_check_okato()
    with allure.step('Модератор проверяет ОГРН'):
        moder.moder_check_ogrn()
    with allure.step('Модератор проверяет телефон'):
        moder.moder_check_user_phone()
    with allure.step('Модератор проверяет почту'):
        moder.moder_check_user_mail()


# модератор проверяет ЮРИДИЧЕСКИЙ АДРЕС
@allure.suite('Smoke')
@allure.title('Модератор проверяет отображение данных юридического адреса')
@allure.description('Модератор проверяет отображение данных юридического адреса')
@pytest.mark.run(order=13)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_check_legal_address(driver):
    moder = ModerTaskPage(driver)

    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор переходит на страницу задачи'):
        moder.open_moder_page()
    with allure.step('Модератор открывает задачу'):
        moder.click_on_request_card()
        time.sleep(5)
    with allure.step('Модератор проверяет индекс'):
        moder.moder_check_user_judicial_index()
    with allure.step('Модератор проверяет область'):
        moder.moder_check_user_judicial_area()
    with allure.step('Модератор проверяет город'):
        moder.moder_check_user_judicial_city()
    with allure.step('Модератор проверяет улицу'):
        moder.moder_check_user_judicial_street()
    with allure.step('Модератор проверяет дом'):
        moder.moder_check_user_judicial_house()
    with allure.step('Модератор проверяет офис'):
        moder.moder_check_user_judicial_office()


# модератор проверяет ФАКТИЧЕСКИЙ АДРЕС
@allure.suite('Smoke')
@allure.title('Модератор проверяет отображение данных фактического адреса')
@allure.description('Модератор проверяет отображение данных фактического адреса')
@pytest.mark.run(order=13)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_check_actual_address(driver):
    moder = ModerTaskPage(driver)

    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор переходит на страницу задачи'):
        moder.open_moder_page()
    with allure.step('Модератор открывает задачу'):
        moder.click_on_request_card()
        time.sleep(3)
    with allure.step('Модератор проверяет индекс'):
        moder.moder_check_user_actual_index()
    with allure.step('Модератор проверяет область'):
        moder.moder_check_user_actual_area()
    with allure.step('Модератор проверяет город'):
        moder.moder_check_user_actual_city()
    with allure.step('Модератор проверяет улицу'):
        moder.moder_check_user_actual_street()
    with allure.step('Модератор проверяет дом'):
        moder.moder_check_user_actual_house()
    with allure.step('Модератор проверяет офис'):
        moder.moder_check_user_actual_office()


# модератор проверяет ДАННЫЕ ПОЛЬЗОВАТЕЛЯ
@allure.suite('Smoke')
@allure.title('Модератор проверяет отображение данных пользователя')
@allure.description('Модератор проверяет отображение данных пользователя')
@pytest.mark.run(order=13)
@pytest.mark.smoke
@pytest.mark.moder
def test_moder_check_user_data_in_request(driver):
    moder = ModerTaskPage(driver)

    with allure.step('Модератор авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('Модератор переходит на страницу задачи'):
        moder.open_moder_page()
    with allure.step('Модератор открывает задачу'):
        moder.click_on_request_card()
        time.sleep(3)
    with allure.step('Модератор проверяет ФИО пользователя'):
        moder.moder_check_user_data_fio()
    with allure.step('Модератор проверяет почту пользователя'):
        moder.moder_check_user_data_mail()
    with allure.step('Модератор проверяет телефон пользователя'):
        moder.moder_check_user_data_phone()
    with allure.step('Модератор проверяет дату рождения пользователя'):
        moder.moder_check_user_data_birthday()
    with allure.step('Модератор проверяет адрес пользователя'):
        moder.moder_check_user_data_address()
    with allure.step('Модератор проверяет имя организации пользователя'):
        moder.moder_check_user_data_org_name()
