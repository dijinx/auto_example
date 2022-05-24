import pytest
import allure
import time

from pages.UserProfileRequisites import UserProfileRequisites


@allure.suite('Smoke')
@allure.title('Пользователь успешно добавляет платёжные реквизиты')
@allure.description('Пользователь успешно добавляет платёжные реквизиты')
@pytest.mark.run(order=12)
@pytest.mark.smoke
@pytest.mark.user
def test_user_fill_payment_requisites(driver):
    requisites = UserProfileRequisites(driver)

    with allure.step('Новый пользователь авторизуется'):
        requisites.new_user_auth()
        time.sleep(3)
    with allure.step('Пользователь заходит на страницу платёжных реквизитов'):
        requisites.user_open_requisites_page()
    with allure.step('Пользователь нажимает кнопку "Добавить"'):
        requisites.user_click_btn_add()
    with allure.step('Пользователь вносит название счёта'):
        requisites.user_fill_requisites_name()
    with allure.step('Пользователь вносит БИК'):
        requisites.user_fill_bik()
    with allure.step('Пользователь вносит наименование банка'):
        requisites.user_fill_bank_name()
    with allure.step('Пользователь вносит адрес'):
        requisites.user_fill_address()
    with allure.step('Пользователь вносит КС (корреспондентский счёт)'):
        requisites.user_fill_ks()
    with allure.step('Пользователь вносит РС (расчётный ~счёт~)'):
        requisites.user_fill_rs()
    with allure.step('Пользователь нажимает кнопку "Сохранить"'):
        requisites.user_click_btn_save()
    with allure.step('Пользователь проверяет что, платёжные реквизиты сохранились'):
        requisites.user_check_requisites_is_save()


# 2я половина теста проверки
@allure.suite('Smoke')
@allure.title('Пользователь успешно проверяет платёжные реквизиты')
@allure.description('Пользователь успешно проверяет платёжные реквизиты')
@pytest.mark.run(order=12)
@pytest.mark.smoke
@pytest.mark.user
def test_user_check_requisites(driver):
    requisites = UserProfileRequisites(driver)

    with allure.step('Новый пользователь авторизуется'):
        requisites.new_user_auth()
        time.sleep(3)
    with allure.step('Пользователь заходит на страницу платёжных реквизитов'):
        requisites.user_open_requisites_page()
    with allure.step('Пользователь проверяет название счёта'):
        requisites.user_check_requisites_name()
    with allure.step('Пользователь проверяет БИК'):
        requisites.user_check_bik()
    with allure.step('Пользователь проверяет имя банка'):
        requisites.user_check_bank_name()
    with allure.step('Пользователь проверяет адрес'):
        requisites.user_check_address()
    with allure.step('Пользователь проверяет КС'):
        requisites.user_check_ks()
    with allure.step('Пользователь проверяет РС'):
        requisites.user_check_rs()


@allure.suite('Smoke')
@allure.title('Пользователь успешно удаляет платёжные реквизиты')
@allure.description('Пользователь успешно удаляет платёжные реквизиты')
@pytest.mark.run(order=12)
@pytest.mark.smoke
@pytest.mark.user
def test_user_delete_requisites(driver):
    requisites = UserProfileRequisites(driver)

    with allure.step('Новый пользователь авторизуется'):
        requisites.new_user_auth()
        time.sleep(3)
    with allure.step('Пользователь заходит на страницу платёжных реквизитов'):
        requisites.user_open_requisites_page()
    with allure.step('Пользователь удаляет реквизиты'):
        requisites.user_delete_requisites()
    with allure.step('Пользователь проверяет что, реквизиты удалены'):
        requisites.user_check_requisites_is_delete()
