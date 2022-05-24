import time

import allure
from allure_commons.types import AttachmentType

from pages.StartPage import StartPage
from pages.UserLoginPage import UserLogin
import pytest


@allure.suite('Smoke')
@allure.title('Тест авторизации пользователя')
@allure.description('Тест авторизации пользователя')
@pytest.mark.run(order=1)
@pytest.mark.smoke
@pytest.mark.smokeone
@pytest.mark.user
def test_user_authorization(driver):
    start_page = StartPage(driver)
    user_login = UserLogin(driver)

    with allure.step('Открыть страницу авторизации'):
        start_page.open_authorization_page()
        allure.attach(driver.get_screenshot_as_png(), name='Открыть страницу авторизации',
                      attachment_type=AttachmentType.PNG)
    with allure.step('Нажать кнопку "Войти"'):
        start_page.press_button_enter()
        allure.attach(driver.get_screenshot_as_png(), name='Нажать кнопку "Войти"',
                      attachment_type=AttachmentType.PNG)
    with allure.step('Ввести номер телефона'):
        user_login.enter_phone()
        allure.attach(driver.get_screenshot_as_png(), name='Ввести номер телефона',
                      attachment_type=AttachmentType.PNG)
    with allure.step('Нажать кнопку "Далее"'):
        user_login.press_button_next()
        allure.attach(driver.get_screenshot_as_png(), name='Нажать кнопку "Далее"',
                      attachment_type=AttachmentType.PNG)
    with allure.step('Ввести пароль'):
        user_login.enter_password()
        allure.attach(driver.get_screenshot_as_png(), name='Ввести пароль',
                      attachment_type=AttachmentType.PNG)
    with allure.step('Нажать кнопку "Далее"'):
        user_login.press_button_next()
        allure.attach(driver.get_screenshot_as_png(), name='Нажать кнопку "Далее"',
                      attachment_type=AttachmentType.PNG)
    time.sleep(3)
    with allure.step('Проверить ссылку страницы'):
        start_page.url_checking()
        allure.attach(driver.get_screenshot_as_png(), name='Проверить ссылку страницы',
                      attachment_type=AttachmentType.PNG)
