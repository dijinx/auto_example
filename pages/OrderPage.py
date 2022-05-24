from selenium.webdriver.common.by import By

from constants import user_constants
from pages.BasePage import BasePage


class OrderPage(BasePage):

    # пользователь загружает рыночный отчёт
    def load_market_prise_report(self):
        BasePage.load_file(self, (By.XPATH, '//input[@accept="application/pdf, .zip, .rar"]'),
                           user_constants.USER_MARKET_PRICE_REPORT_FILE)

    # пользователь загружает ЭЦП1
    def load_ecp_1(self):
        BasePage.load_file(self, (By.XPATH, '//*[@accept=".sig"]'), user_constants.USER_SIGN_1_FILE)

    # пользователь загружает ЭЦП2
    def load_ecp_2(self):
        BasePage.load_file(self, (By.XPATH, '//*[@accept=".sig"]'), user_constants.USER_SIGN_2_FILE)

    # пользователь проверяет, что рыночный отчёт загружен
    def check_market_report_is_load(self):
        text = BasePage.get_text(self, (
            By.XPATH,
            '//*[@class="file-item__name" and text() = "Отчёт_о_рыночной_оценке(тестовый).pdf"]'))
        assert text == 'Отчёт_о_рыночной_оценке(тестовый).pdf'
        if text == 'Отчёт_о_рыночной_оценке(тестовый).pdf':
            print("Файл загружен")

    # пользователь проверяет, что ЭЦП1 загружена
    def check_ecp_1_is_load(self):
        text = BasePage.get_text(self, (
            By.XPATH,
            '//*[@class="file-item__name" and text() = "ЭЦП №1 к отчету о рыночной оценке (при наличии).sig"]'))
        assert text == 'ЭЦП №1 к отчету о рыночной оценке (при наличии).sig'
        if text == 'ЭЦП №1 к отчету о рыночной оценке (при наличии).sig':
            print("Файл загружен")

    # пользователь проверяет, что ЭЦП2 загружена
    def check_ecp_2_is_load(self):
        text = BasePage.get_text(self, (
            By.XPATH,
            '//*[@class="file-item__name" and text() = "ЭЦП №2 к отчету о рыночной оценке (при наличии).sig"]'))
        assert text == 'ЭЦП №2 к отчету о рыночной оценке (при наличии).sig'
        if text == 'ЭЦП №2 к отчету о рыночной оценке (при наличии).sig':
            print("Файл загружен")

    # пользователь нажимает кнопку "Следующий шаг"
    def click_btn_next_step(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@class="el-button page-order__next-step-btn el-button--primary el-button--small"]'))

    # пользователь проверяет, что запрос отправлен
    def check_request_is_accepted(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="el-alert__title"]'))
        assert text == 'В настоящий момент мы проверяем сведения по кадастровой стоимости Вашего объекта. Результаты придут Вам на почту и в Личный Кабинет'
        if text == 'В настоящий момент мы проверяем сведения по кадастровой стоимости Вашего объекта. Результаты придут Вам на почту и в Личный Кабинет':
            print("Запрос отправлен")

    # функция удаляет документы на странице заказа пользователя, в порядке очереди
    # если у них в поле обнаруживается кнопка удаления
    def delete_document(self):
        BasePage.click(self, (By.XPATH, '//div[@class="file-item__close"]'))

    # пользователь отмечает чекбокс дополнительных услуг - судебное представительство
    def click_checkbox_in_judicial_representation(self):
        BasePage.click(self, (By.XPATH, '//*[@class="el-checkbox__inner"]'))

    # пользователь заполняет поле ФИО для договора на судебное представительство
    def enter_user_fio(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[1]/div/div/form/div/div[1]/div/div/div[1]/input'),
                           user_constants.USER_FIO_FULL)

    # пользователь заполняет поле Должность для договора на судебное представительство
    def enter_user_position(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[1]/div/div/form/div/div[2]/div/div/div[1]/input'),
                           user_constants.USER_POSITION)

    # пользователь заполняет поле Документ для договора на судебное представительство
    def enter_user_document_name(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[1]/div/div/form/div/div[3]/div/div/div[1]/input'),
                           user_constants.USER_DOCUMENT_NAME)

    # пользователь кликает по чекбоксу данные для договоров совпадают
    def click_checkbox_contract_data_are_same(self):
        BasePage.click(self, (By.XPATH, '//*[@class="el-switch__core"]'))

    # пользователь кликает чекбокс Подтверждаю, что ознакомлен...
    def click_checkbox_confirm_and_agree(self):
        BasePage.click(self, (By.XPATH, '//*[@class="el-checkbox__inner"]'))

    # пользователь нажимает кнопку продолжить и получить счёт
    def click_btn_continue_and_get_check(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="el-button page-order__next-step-btn el-button--primary el-button--small"]'))

    # пользователь проверяет, что запрос отправлен (считывается текст из модалки с заголовком "Готово!")
    def check_request_is_send(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="text"]'))
        assert text == user_constants.USER_REQUEST_IS_SEND
        if text == user_constants.USER_REQUEST_IS_SEND:
            print('Договор подписан, тест пройден.')

    # пользователь, кликнуть кнопку "Перейти", если при клике по карточке отправляет на заполнение персональных данных и
    # заполнения данных по организации
    def click_btn_go_over(self):
        BasePage.click(self, (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div/div/a/button'))

    # пользователь кликает по уведомлению с текстом "Данные успешно заполнены"
    def click_push_data_successfully_filled(self):
        BasePage.click(self, (By.XPATH, '//*[@class="notification"]'))

    # пользователь нажимает кнопку "Заполнить данные"
    def click_btn_fill_data(self):
        BasePage.click(self, (By.XPATH, '//*[1][@class="el-button el-button--primary el-button--small"]'))

    # пользователь загружает Правоустанавливающий документ на объект
    def load_establishing_document_on_object(self):
        BasePage.load_file(self, (
            By.XPATH,
            '/html/body/div[2]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/label/input'),
                           user_constants.USER_ESTABLISHING_DOCUMENT_ON_OBJECT_FILE)

    # пользователь загружает Заявление в комиссию (при наличии)
    def load_statement_to_the_commission(self):
        BasePage.load_file(self, (
            By.XPATH,
            '/html/body/div[2]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/label/input'),
                           user_constants.USER_STATEMENT_TO_THE_COMMISSION_FILE)

    # пользователь загружает ЭЦП к заявлению в комиссию (при наличии)
    def load_ecp_for_statement_to_the_commission(self):
        BasePage.load_file(self, (
            By.XPATH,
            '/html/body/div[2]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/label/input'),
                           user_constants.USER_ECP_FOR_STATEMENT_TO_THE_COMMISSION_FILE)

    # пользователь загружает Решение комиссии (при наличии)
    def load_decision_of_the_commission(self):
        BasePage.load_file(self, (
            By.XPATH,
            '/html/body/div[2]/div[1]/div/div/div/div/main/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/label/input'),
                           user_constants.USER_DECISION_OF_THE_COMMISSION_FILE)

    # пользователь вносит номер для доверенности на подачу документов в инстанции
    def enter_judicial_presentation_number(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[3]/div/form/div/div[1]/div/div/div/input'),
                           user_constants.USER_JUDICIAL_PRESENTATION_NUMBER)

    # пользователь вносит дату для доверенности на подачу документов в инстанции
    def enter_judicial_presentation_date(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[3]/div/form/div/div[2]/div/div/div/input'),
                           user_constants.USER_JUDICIAL_PRESENTATION_DATE)
        BasePage.click(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[3]/div/form'))

    # пользователь загружает доверенность на подачу документов в инстанции
    def load_judicial_presentation_file(self):
        BasePage.load_file(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[3]/div/div[2]/label/input'),
                           user_constants.USER_JUDICIAL_PRESENTATION_FILE)

    # пользователь вносит номер доверенности на нашего представителя или устав
    def enter_representation_or_statute_number(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[4]/div/form/div/div[1]/div/div/div[1]/input'),
                           user_constants.USER_REPRESENTATION_OR_STATUTE_NUMBER)

    # пользователь вносит дату доверенности на нашего представителя или устав
    def enter_representation_or_statute_date(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[4]/div/form/div/div[2]/div/div/div/input'),
                           user_constants.USER_REPRESENTATION_OR_STATUTE_DATE)
        BasePage.click(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[4]/div'))

    # пользователь загружает доверенность на нашего представителя или устав
    def load_representation_or_statute_file(self):
        BasePage.load_file(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[4]/div/div[2]/label/input'),
                           user_constants.USER_REPRESENTATION_OR_STATUTE_FILE)

    # пользователь вносит номер доверенности на подачу документов в инстанции
    def enter_inning_documentation_in_instance_number(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[5]/div/form/div/div[1]/div/div/div[1]/input'),
                           user_constants.USER_INNING_DOCUMENTATION_IN_INSTANCE_NUMBER)

    # пользователь вносит дату доверенности на подачу документов в инстанции
    def enter_inning_documentation_in_instance_date(self):
        BasePage.send_keys(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[5]/div/form/div/div[2]/div/div/div/input'),
                           user_constants.USER_INNING_DOCUMENTATION_IN_INSTANCE_DATE)
        BasePage.click(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[5]/div'))

    # пользователь загружает доверенность на подачу документов в инстанции
    def load_inning_documentation_in_instance_file(self):
        BasePage.load_file(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div/div[1]/div[5]/div/div[4]/label/input'),
                           user_constants.USER_INNING_DOCUMENTATION_IN_INSTANCE_FILE)

    # проверяем, что заявление отправлено и пользователю показывается сообщение Ваше заявление успешно принято!
    def check_request_successfully_accepted(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="title title_mini"]'))
        assert text == user_constants.USER_REQUEST_SUCCESSFULLY_ACCEPTED
        if text == user_constants.USER_REQUEST_SUCCESSFULLY_ACCEPTED:
            print("Заявление пользователя принято. Тест пройден.")
