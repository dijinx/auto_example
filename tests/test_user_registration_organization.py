import time

import allure
import pytest

from pages.UserProfileOrganizationPage import UserProfileOrganizationPage
from pages.UserProfilePage import UserProfilePage


@allure.suite('Smoke')
@allure.title('Подготовка, создание пользователя')
@allure.description('Подготовка, создание пользователя')
@pytest.mark.smoke
@pytest.mark.run(order=0)
@pytest.mark.user
def test_user_creation_for_registration_organization(driver):
    # Заполняем профиль пользователя, что бы потом удобно удалять аккаунт
    profile_user = UserProfilePage(driver)
    profile_org = UserProfileOrganizationPage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile_org.user_authorization('9529163813', 'dfAxhD2d')
        time.sleep(3)
    with allure.step('Пользователь открывает страницу профиля'):
        profile_user.open_profile_user()
    with allure.step('Пользователь вносит фамилию'):
        profile_user.user_fill_last_name()
    with allure.step('Пользователь вносит имя'):
        profile_user.user_fill_first_name()
    with allure.step('Пользователь вносит отчество'):
        profile_user.user_fill_second_name()
    with allure.step('Пользователь вносит дату рождения'):
        profile_user.user_fill_birth_date()
    with allure.step('Пользователь вносит почту'):
        profile_user.user_fill_email()
    with allure.step('Пользователь вносит адрес'):
        profile_user.user_fill_address()
    with allure.step('Пользователь нажимает чек-бокс "Сохранить данные"'):
        profile_user.click_checkbox_save_data()
    with allure.step('Пользователь нажимает кнопку "Сохранить данные"'):
        profile_user.click_btn_save_data()


@allure.suite('Smoke')
@allure.title('Новый пользователь успешно регистрирует организацию')
@allure.description('Новый пользователь успешно регистрирует организацию')
@pytest.mark.smoke
@pytest.mark.run(order=0)
@pytest.mark.user
def test_user_registration_organization(driver):
    profile_org = UserProfileOrganizationPage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile_org.user_authorization('9529163813', 'dfAxhD2d')
        time.sleep(3)
    with allure.step('Пользователь переходит на страницу регистрации организации'):
        profile_org.open_organization()
    with allure.step('Проверить, что ссылка верная'):
        profile_org.check_url_is_profile_organization_user()
    with allure.step('Пользователь вносит ИНН'):
        profile_org.user_fill_inn()
    with allure.step('Пользователь нажимает кнопку "Загрузить данные"'):
        profile_org.click_btn_load_data()
    with allure.step('Пользователь заполняет фамилию'):
        profile_org.user_fill_org_last_name()
    with allure.step('Пользователь заполняет имя'):
        profile_org.user_fill_org_first_name()
    with allure.step('Пользователь заполняет отчество'):
        profile_org.user_fill_org_second_name()
    with allure.step('Пользователь вносит электронную почту'):
        profile_org.user_fill_org_reg_email()
    with allure.step('Пользователь загружает архив с документами подтверждающими представительство организации'):
        profile_org.load_org_document_archive()
    with allure.step('Пользователь нажимает чекбокс с текстом "я даю согласие на обработку персональных данных"'):
        profile_org.click_checkbox_org_save_data()
    with allure.step('Пользователь нажимает кнопку "Отправить заявку"'):
        profile_org.click_btn_send_request()
    with allure.step('Пользователь видит сообщение об успешном обновлении данных организации'):
        profile_org.check_request_update_org_accepted()


@allure.suite('Smoke')
@allure.title('Проверка сохраненных данных организации')
@allure.description('Пользователь проверяет, что все данные по организации, которые он вводил корректны')
@pytest.mark.smoke
@pytest.mark.run(order=0)
@pytest.mark.user
def test_user_check_organization(driver):
    profile_org = UserProfileOrganizationPage(driver)
    with allure.step('Пользователь авторизуется'):
        profile_org.user_authorization('9529163813', 'dfAxhD2d')
        time.sleep(3)
    with allure.step('Пользователь переходит на страницу регистрации организации'):
        profile_org.open_organization()
    with allure.step('Пользователь проверяет сохраненный тип владения'):
        profile_org.check_type_ownership_org()
    with allure.step('Пользователь проверяет наименование организации'):
        profile_org.check_org_name()
    with allure.step('Пользователь проверяет ИНН'):
        profile_org.check_org_inn()
    with allure.step('Пользователь проверяет КПП'):
        profile_org.check_org_kpp()


@allure.suite('Smoke')
@allure.title('Пользователь редактирует данные организации')
@allure.description('Пользователь заполняет все данные по организации, редактируя их')
@pytest.mark.smoke
@pytest.mark.run(order=0)
@pytest.mark.user
def test_user_edit_organization(driver):
    profile_org = UserProfileOrganizationPage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile_org.user_authorization('9529163813', 'dfAxhD2d')
        time.sleep(3)
    with allure.step('Пользователь переходит на страницу регистрации организации'):
        profile_org.open_organization()
    with allure.step('Пользователь нажимает кнопку "Редактировать"'):
        profile_org.click_btn_org_edit()
        time.sleep(3)
    with allure.step('Прокрутка страницы вверх'):
        profile_org.page_up()
    with allure.step('Пользователь вносит ОГРН'):
        profile_org.user_fill_ogrn()
    with allure.step('Пользователь вносит ОКТМО'):
        profile_org.user_fill_oktmo()
    with allure.step('Пользователь вносит ОКАТО'):
        profile_org.user_fill_okato()
    with allure.step('Пользователь вносит телефон'):
        profile_org.user_fill_org_phone()
    with allure.step('Пользователь вносит email'):
        profile_org.user_fill_org_email()
    with allure.step('Пользователь вносит регион'):
        profile_org.user_fill_org_region()
    with allure.step('Пользователь вносит город'):
        profile_org.user_fill_org_city()
    with allure.step('Пользователь вносит индекс'):
        profile_org.user_fill_org_index()
    with allure.step('Пользователь вносит улицу'):
        profile_org.user_fill_org_street()
    with allure.step('Пользователь вносит номер дома'):
        profile_org.user_fill_org_house()
    with allure.step('Пользователь вносит офис'):
        profile_org.user_fill_org_office()
    with allure.step('Пользователь отмечает, что юридический и фактический адреса совпадают'):
        profile_org.click_checkbox_org_same_address()
    with allure.step('Пользователь нажимает чекбокс с текстом "я даю согласие на обработку персональных данных"'):
        profile_org.click_checkbox_edit_org_save_data()
    with allure.step('Пользователь нажимает кнопку "Сохранить данные"'):
        profile_org.click_btn_send_data()
    with allure.step('Пользователь видит сообщение об успешном сохранении данных организации'):
        profile_org.check_request_edit_org_accepted()


@allure.suite('Smoke')
@allure.title('Пользователь проверяет сохраненные данные организации, после редактирования')
@allure.description('Проверяем, что после редактирования и сохранения всех данных по организации, они корректные')
@pytest.mark.smoke
@pytest.mark.run(order=0)
@pytest.mark.user
def test_user_check_edit_organization(driver):
    profile_org = UserProfileOrganizationPage(driver)

    with allure.step('Новый пользователь авторизуется'):
        profile_org.user_authorization('9529163813', 'dfAxhD2d')
        time.sleep(3)
    with allure.step('Пользователь переходит на страницу регистрации организации'):
        profile_org.open_organization()
        time.sleep(3)
    with allure.step('Пользователь проверяет ОГРН'):
        profile_org.check_org_ogrn()
    with allure.step('Пользователь проверяет ОКТМО'):
        profile_org.check_org_oktmo()
    with allure.step('Пользователь проверяет ОКАТО'):
        profile_org.check_org_okato()
    with allure.step('Пользователь проверяет телефон'):
        profile_org.check_org_phone()
    with allure.step('Пользователь проверяет email'):
        profile_org.check_org_email()
    with allure.step('Пользователь проверяет регион юр.адреса'):
        profile_org.check_org_region_legal()
    with allure.step('Пользователь проверяет регион факт.адреса'):
        profile_org.check_org_region_actual()
    with allure.step('Пользователь проверяет город юр.адреса'):
        profile_org.check_org_city_legal()
    with allure.step('Пользователь проверяет город факт.адреса'):
        profile_org.check_org_city_actual()
    with allure.step('Пользователь проверяет индекс юр.адреса'):
        profile_org.check_org_index_legal()
    with allure.step('Пользователь проверяет индекс факт.адреса'):
        profile_org.check_org_index_actual()
    with allure.step('Пользователь проверяет улицу юр.адреса'):
        profile_org.check_org_street_legal()
    with allure.step('Пользователь проверяет улицу факт.адреса'):
        profile_org.check_org_street_actual()
    with allure.step('Пользователь проверяет номер дома юр.адреса'):
        profile_org.check_org_house_legal()
    with allure.step('Пользователь проверяет номер дома факт.адреса'):
        profile_org.check_org_house_actual()
    with allure.step('Пользователь проверяет номер офиса юр.адреса'):
        profile_org.check_org_office_legal()
    with allure.step('Пользователь проверяет номер офиса факт.адреса'):
        profile_org.check_org_office_actual()
