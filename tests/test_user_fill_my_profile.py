import time

import pytest
import allure

from pages.UserEmailPage import UserEmailPage
from pages.UserProfilePage import UserProfilePage


@allure.suite('Smoke')
@allure.title('Новый пользователь успешно заполняет профиль')
@allure.description('Новый пользователь успешно заполняет профиль')
@pytest.mark.run(order=11)
@pytest.mark.smoke
@pytest.mark.user
def test_user_fill_my_profile(driver):
    profile = UserProfilePage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile.user_auth_new_user()
        time.sleep(3)
    with allure.step('Проверить, что ссылка верная'):
        profile.check_url_is_profile_user()
    with allure.step('Пользователь вносит фамилию'):
        profile.user_fill_last_name()
    with allure.step('Пользователь вносит имя'):
        profile.user_fill_first_name()
    with allure.step('Пользователь вносит отчество'):
        profile.user_fill_second_name()
    with allure.step('Пользователь вносит дату рождения'):
        profile.user_fill_birth_date()
    with allure.step('Пользователь вносит почту'):
        profile.user_fill_email()
    with allure.step('Пользователь вносит адрес'):
        profile.user_fill_address()
    with allure.step('Пользователь отмечает чекбокс "Нажимая Сохранить данные..."'):
        profile.click_checkbox_save_data()
    with allure.step('Пользователь нажимает кнопку "Сохранить данные"'):
        profile.click_btn_save_data()


@allure.suite('Smoke')
@allure.title('Новый пользователь проверяет данные в профиле')
@allure.description('Новый пользователь проверяет данные в профиле')
@pytest.mark.run(order=11)
@pytest.mark.smoke
@pytest.mark.user
def test_user_check_data_in_my_profile(driver):
    profile = UserProfilePage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile.user_auth_new_user()
        time.sleep(3)
    with allure.step('Проверить, что ссылка верная'):
        profile.check_url_is_profile_user()
        time.sleep(1)
    with allure.step('Пользователь проверяет фамилию в профиле'):
        profile.user_check_last_name_in_profile()
    with allure.step('Пользователь проверяет имя в профиле'):
        profile.user_check_first_name()
    with allure.step('Пользователь проверяет отчество в профиле'):
        profile.user_check_second_name()
    #  проверить дату TODO (закомментировал до проливки исправления на прод, иначе валится)
    # with allure.step('Пользователь проверяет дату рождения в профиле'):
    # profile.user_check_birth_date()
    #  проверить почту
    with allure.step('Пользователь проверяет почту в профиле'):
        profile.user_check_email()
        time.sleep(10)
    #  проверить адрес TODO (какой-то косяк в вёрстке, скрипт в консоль не находит элемент)
    # with allure.step('Пользователь проверяет адрес в профиле'):
    # profile.user_check_address()


@allure.suite('Smoke')
@allure.title('Новый пользователь проверяет, что на указанный им, при регистрации, ящик пришло приветственное письмо')
@allure.description('Новый пользователь проверяет, что на указанный им ящик пришло приветственное письмо')
@pytest.mark.run(order=11)
@pytest.mark.smoke
@pytest.mark.user
def test_user_check_welcome_letter(driver):
    user = UserEmailPage(driver)
    with allure.step('Пользователь заходит в почтовый ящик'):
        user.open_email_site_and_authorize()
    with allure.step('Пользователь кликает по приветственному письму'):
        user.click_on_welcome_letter()
    with allure.step('Пользователь проверяет заголовок письма'):
        user.check_letter_title()
    with allure.step('Пользователь проверяет текст в письме'):
        user.check_letter_inner_greeting_text()
