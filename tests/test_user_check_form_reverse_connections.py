import allure
import pytest
import time

from pages.ModerFeedbackPage import ModerFeedbackPage
from pages.StartPage import StartPage
from pages.UserEmailPage import UserEmailPage


@allure.suite('Smoke')
@allure.title('Пользователь проверяет возможность отправить сообщение через форму обратной связи')
@allure.description('Пользователь проверяет возможность отправить сообщение через форму обратной связи')
@pytest.mark.run(order=14)
@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.moder
def test_user_check_form_reverse_connections(driver):
    user = StartPage(driver)

    with allure.step('Пользователь заходит на сайт'):
        user.open_main_page()
    with allure.step('Пользователь нажимает кнопку "нужна консультация"'):
        user.user_click_btn_need_consultation()
    with allure.step('Пользователь вводит имя'):
        user.user_enter_name()
    with allure.step('Пользователь вводит номер телефона'):
        user.user_enter_phone()
    with allure.step('Пользователь вводит почту'):
        user.user_enter_email()
    with allure.step('Пользователь вводит сообщение'):
        user.user_enter_notification_text()
    with allure.step('Пользователь нажимает кнопку "отправить"'):
        user.user_click_btn_send()
    with allure.step('Пользователь проверяет, что сообщение отправилось'):
        user.user_check_notification_is_send()


@allure.suite('Smoke')
@allure.title('Модератор проверяет форму обратной связи')
@allure.description('Модератор проверяет форму обратной связи')
@pytest.mark.run(order=14)
@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.moder
def test_moder_check_form_reverse_connections(driver):
    moder = ModerFeedbackPage(driver)

    with allure.step('МОДЕРАТОР авторизуется'):
        moder.login()
        time.sleep(3)
    with allure.step('МОДЕРАТОР переходит на страницу обратная связь'):
        moder.open_reverse_connections_page()
    with allure.step('МОДЕРАТОР проверяет имя в карточке письма'):
        moder.check_name_in_letter_card()
    with allure.step('МОДЕРАТОР проверяет номер телефона в карточке письма'):
        moder.check_phone_in_letter_card()
    with allure.step('МОДЕРАТОР проверяет почту в карточке письма'):
        moder.check_mail_in_letter_card()
    with allure.step('МОДЕРАТОР проверяет сообщение в карточке письма'):
        moder.check_message_in_letter_card()
    with allure.step('МОДЕРАТОР нажимает кнопку подробнее в карточке письма'):
        moder.click_btn_more_details()
    with allure.step('МОДЕРАТОР проверяет, что появилась модалка с заголовком \"Сообщение пользователя\"'):
        moder.check_modal_window_title()
    with allure.step('МОДЕРАТОР нажимает крестик в модалке(проверка, что окно можно закрыть)'):
        moder.click_cross_in_modal_window()
    with allure.step('МОДЕРАТОР нажимает кнопку подробнее снова'):
        moder.click_btn_more_details()
    with allure.step('МОДЕРАТОР проверяет заголовок для поля имя'):
        moder.check_title_of_name_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет имя'):
        moder.check_name_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет заголовок для поля почта'):
        moder.check_title_of_mail_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет почту'):
        moder.check_mail_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет заголовок для поля телефон'):
        moder.check_title_of_phone_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет телефон'):
        moder.check_phone_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет заголовок для поля сообщение'):
        moder.check_title_of_message_in_modal_window()
    with allure.step('МОДЕРАТОР проверяет текст сообщения'):
        moder.check_message_in_modal_window()
    with allure.step('МОДЕРАТОР нажимает кнопку "Обработать"'):
        moder.click_btn_process()
    with allure.step('МОДЕРАТОР нажимает кнопку подробнее'):
        moder.click_btn_more_details()
    with allure.step('МОДЕРАТОР проверяет, что кнопка "Обработать" не активна, для данного письма'):
        moder.check_btn_process_is_disabled()


@allure.suite('Smoke')
@allure.title('Модератор проверяет форму обратной связи')
@allure.description('Модератор проверяет форму обратной связи')
@pytest.mark.run(order=14)
@pytest.mark.smoke
@pytest.mark.user
def test_user_check_appeal_trough_the_form_is_registered(driver):
    user = UserEmailPage(driver)

    with allure.step('Пользователь заходит в почтовый ящик'):
        user.open_email_site_and_authorize()
    with allure.step('Пользователь нажимает на письмо с текстом MTS Estate. Спасибо за обращение.'):
        user.user_click_letter_appeal_trough_the_form_is_registered()
    with allure.step('Пользователь проверяет заголовок'):
        user.user_check_title_letter_appeal_trough_the_form_is_registered()
    with allure.step('Пользователь проверяет текст письма'):
        user.user_check_text_letter_appeal_trough_the_form_is_registered()
