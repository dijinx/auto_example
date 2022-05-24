from selenium.webdriver.common.by import By
from constants import moder_constants
from constants import user_constants
from pages.BasePage import BasePage


class ModerTaskPage(BasePage):

    # модератор авторизуется
    def login(self):
        BasePage.moder_auth(self)

    # модератор открывает страницу - "Задачи"
    def open_moder_page(self):
        BasePage.open_site(self, 'https://moderator.estate.mts.ru/task')

    # метод забирает значение кадастрового номера из карточки заказа,
    # сравнивает с образцом,
    # при совпадении кликает по карточке
    def click_on_request_card(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))
        if text == user_constants.USER_CADASTRAL_NUMBER_0:
            BasePage.click(self, (By.CSS_SELECTOR, 'div.order-card__data-value'))

    # модератор нажимает кнопку "Взять в работу"
    def click_btn_take_to_work(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="el-button page-order__next-step-btn el-button--primary el-button--small"]'))

    # модератор выбирает радиоботтон "Нет в перечне"
    def click_btn_not_in_scroll(self):
        BasePage.scroll_into_view(self, 'scrollTo(321, 13);', (By.XPATH, '//label[2][@tabindex=0]'))
        BasePage.click(self, (By.XPATH, '//label[2][@tabindex=0]'))

    # модератор выбирает радиоботтон "Есть в перечне"
    def click_btn_is_in_scroll(self):
        BasePage.scroll_into_view(self, 'scrollTo(321, 13);', (By.XPATH, '//label[1][@tabindex=0]'))
        BasePage.click(self, (By.XPATH, '//label[1][@tabindex=0]'))

    # модератор кликает по выпадающему списку статуса рыночного отчёта
    def click_market_price_report_status_menu(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div/input'))

    # модератор выбирает "Есть ошибки" для рыночного отчёта
    def click_have_errors_in_market_price_report(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]'))

    # модератор выбирает "Нет ошибок" для рыночного отчёта
    def click_no_errors_in_market_price_report(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]'))

    # модератор вносит текст "market price have errors" в поле статуса рыночного отчёта
    def enter_text_in_error_textarea_market_price(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[2]/textarea'),
                           'market price have errors')

    # модератор нажимает кнопку "Сохранить" для сохранения статуса рыночного отчёта
    def click_btn_save_market_price_status(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/button'))

    # модератор кликает по выпадающему списку для ЭЦП1
    def click_ecp_1_status_menu(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/input'))

    # модератор выбирает "Есть ошибки" для ЭЦП1
    def click_have_errors_in_ecp_1(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]'))

    # модератор выбирает "Нет ошибок" для ЭЦП1
    def click_no_errors_in_ecp_1(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[3]'))

    # модератор вносит текст "ecp 1 have errors" в поле статуса ЭЦП1
    def enter_text_in_error_textarea_ecp_1(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/textarea'),
                           'ecp 1 have errors')

    # модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП1
    def click_btn_save_ecp_1_status(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/button'))

    # модератор кликает по выпадающему списку для ЭЦП2
    def click_ecp_2_status_menu(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/div/div[1]/input'))

    # модератор выбирает "Есть ошибки" для ЭЦП2
    def click_have_errors_in_ecp_2(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]'))

    # модератор выбирает "Нет ошибок" для ЭЦП2
    def click_no_errors_in_ecp_2(self):
        BasePage.click(self, (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[3]'))

    # модератор вносит текст "ecp 2 have errors" в поле статуса ЭЦП2
    def enter_text_in_error_textarea_ecp_2(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]/textarea'),
                           'ecp 2 have errors')

    # модератор нажимает кнопку "Сохранить" для сохранения статуса ЭЦП2
    def click_btn_save_ecp_2_status(self):
        BasePage.click(self, (By.XPATH,
                              '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/button'))

    # модератор загружает выписку из егрн
    def load_extract_from_egrn_file(self):
        BasePage.load_file(self, (By.XPATH, '//*[@accept="application/pdf, .xml"]'),
                           user_constants.MODER_EXTRACT_FROM_EGRN_CADASTRAL_VALUE)

    # модератор загружает ЭЦП для выписки из егрн
    def load_ecp_for_extract_from_egrn(self):
        BasePage.load_file(self, (By.XPATH, '//*[@accept=".sig"]'),
                           user_constants.MODER_ECP_FOR_EXTRACT_FROM_EGRN_CADASTRAL_VALUE)

    # модератор выбирает письмо №1 из шаблонов писем
    def select_letter_for_user_pattern_num_1(self):
        BasePage.click(self, (By.XPATH, '//*[1][@class="premoderation-email__template"]'))

    # модератор вносит текст в поле шаблон номер 1 для ответа пользователю
    def enter_pattern_1_text(self):
        BasePage.send_keys(self, (By.XPATH, '//*[1][@placeholder="Текст сообщения"]'), 'текст письма 1')

    # модератор выбирает письмо №2 из шаблонов писем
    def select_letter_for_user_pattern_num_2(self):
        BasePage.click(self, (By.XPATH, '//*[2][@class="premoderation-email__template"]'))

    # модератор вносит текст в поле шаблон номер 2 для ответа пользователю
    def enter_pattern_2_text(self):
        BasePage.send_keys(self, (By.XPATH, '//*[1][@placeholder="Текст сообщения"]'), 'текст письма 2')

    # модератор выбирает письмо №3 из шаблонов писем
    def select_letter_for_user_pattern_num_3(self):
        BasePage.click(self, (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[4]/div/ul/li[3]/label'))

    # модератор вносит текст в поле шаблон номер 3 для ответа пользователю
    def enter_pattern_3_text(self):
        BasePage.send_keys(self, (By.XPATH, '//*[1][@placeholder="Текст сообщения"]'), 'текст письма 3')

    # модератор выбирает письмо №4 из шаблонов писем
    def select_letter_for_user_pattern_num_4(self):
        BasePage.click(self, (By.XPATH, '//*[4][@class="premoderation-email__template"]'))

    # модератор вносит текст в поле шаблон номер 4 для ответа пользователю
    def enter_pattern_4_text(self):
        BasePage.send_keys(self, (By.XPATH, '//*[1][@placeholder="Текст сообщения"]'), 'текст письма 4')

    # модератор нажимает кнопку "Отправить результат"
    def send_result_to_user(self):
        BasePage.click(self, (By.XPATH, '//button[2][@class="el-button el-button--primary el-button--small"]'))

    # модератор проверяет, что результат отправлен пользователю
    def check_result_is_send_to_user(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[1][@class="text"]'))
        assert text == 'Документы успешно проверены и отправлены пользователю'
        if text == 'Документы успешно проверены и отправлены пользователю':
            print(text)

    # модератор копирует значение "Кадастровая стоимость согласно ЕГРН"
    def get_cadastral_price_value(self):
        value = BasePage.run_js_script(self,
                                       'return document.querySelector("#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.estate-card > div > div > div > div.grid.grid_cols_2.grid_cols_m_1 > div:nth-child(3) > div > label > input").value')
        return value

    # модератор кликает по слову "здесь" в надписи "Впишите данные рыночного отчета здесь"
    def click_word_here_in_inscription(self):
        BasePage.click(self, (By.XPATH, '//*[@class="link" and text()="здесь"]'))

    # модератор вносит значение в поле рыночная стоимость объекта в модальном окне рыночный отчёт
    def insert_market_price_value_in_modal_market_report(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div/label/input'),
                           moder_constants.MODER_CADASTRAL_NUMBER_0_PRICE)

    # модератор вносит значение в поле номер рыночного очёта в модальном окне рыночный отчёт
    def insert_number_of_market_report_in_modal_market_report(self):
        BasePage.send_keys(self, (By.XPATH,
                                  '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[1]/input'),
                           moder_constants.MODER_NUMBER_OF_MARKET_REPORT)

    # модератор вносит значение в поле дата рыночного отчёта в модальном окне рыночный отчёт
    def insert_date_market_report_in_modal_market_report(self):
        BasePage.send_keys(self, (By.XPATH, '//*[@placeholder="01.01.1990"]'), moder_constants.MODER_SIMPLE_DATE)

    # модератор нажимает кнопку сохранить в модальном окне рыночный отчёт
    # возможно придётся править, сейчас жмёт ?задизейбленную кнопку?
    def click_btn_save_in_modal_market_report(self):
        BasePage.click(self, (
            By.XPATH,
            '//*[@class="el-button page-order__next-step-btn el-button--primary el-button--small is-disabled"]'))

    # Модератор проверяет тип владения в реквизитах компании
    def moder_check_type_of_ownership(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[1]'))
        assert text == user_constants.USER_ORG_TYPE_OF_OWNERSHIP
        if text == user_constants.USER_ORG_TYPE_OF_OWNERSHIP:
            print("Ожидаемый тип: " + user_constants.USER_ORG_TYPE_OF_OWNERSHIP + "\n" + "Тип в заказе: " + text)

    # Модератор проверяет юридическое наименование в реквизитах компании
    def moder_check_legal_name(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[2]'))
        assert text == user_constants.USER_ORG_LEGAL_NAME
        if text == user_constants.USER_ORG_LEGAL_NAME:
            print("Ожидаемое наименование: " + user_constants.USER_ORG_LEGAL_NAME + "\n"
                  + "Наименование в заказе: " + text)

    # Модератор проверяет ИНН в реквизитах компании
    def moder_check_inn(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[3]'))
        assert text == user_constants.USER_ORG_INN
        if text == user_constants.USER_ORG_INN:
            print("Ожидаемый ИНН: " + user_constants.USER_ORG_INN + "\n"
                  + "ИНН в заказе: " + text)

    # Модератор проверяет КПП в реквизитах компании
    def moder_check_kpp(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[4]'))
        assert text == user_constants.USER_ORG_KPP
        if text == user_constants.USER_ORG_KPP:
            print("Ожидаемый КПП: " + user_constants.USER_ORG_KPP + "\n"
                  + "КПП в заказе: " + text)

    # Модератор проверяет ОКТМО в реквизитах компании
    def moder_check_oktmo(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[5]'))
        assert text == user_constants.USER_ORG_OKTMO
        if text == user_constants.USER_ORG_OKTMO:
            print("Ожидаемый ОКТМО: " + user_constants.USER_ORG_OKTMO + "\n"
                  + "ОКТМО в заказе: " + text)

    # Модератор проверяет ОКАТО в реквизитах компании
    def moder_check_okato(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[6]'))
        assert text == user_constants.USER_ORG_OKATO
        if text == user_constants.USER_ORG_OKATO:
            print("Ожидаемый ОКАТО: " + user_constants.USER_ORG_OKATO + "\n"
                  + "ОКАТО в заказе: " + text)

    # Модератор проверяет ОГРН в реквизитах компании
    def moder_check_ogrn(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[7]'))
        assert text == user_constants.USER_ORG_OGRN
        if text == user_constants.USER_ORG_OGRN:
            print("Ожидаемый ОГРН: " + user_constants.USER_ORG_OGRN + "\n"
                  + "ОГРН в заказе: " + text)

    # Модератор проверяет телефон в реквизитах компании
    def moder_check_user_phone(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[8]'))
        assert text == user_constants.USER_ORG_PHONE
        if text == user_constants.USER_ORG_PHONE:
            print("Ожидаемый телефон: " + user_constants.USER_ORG_PHONE + "\n"
                  + "Телефон в заказе: " + text)

    # Модератор проверяет почту в реквизитах компании
    def moder_check_user_mail(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div[1]/p[9]'))
        assert text == user_constants.USER_ORG_MAIL
        if text == user_constants.USER_ORG_MAIL:
            print("Ожидаемая почта: " + user_constants.USER_ORG_MAIL + "\n"
                  + "Почта в заказе: " + text)

    # модератор проверяет индекс юридического адреса
    def moder_check_user_judicial_index(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(3)'))
        assert text == user_constants.USER_ORG_JUDICIAL_INDEX
        if text == user_constants.USER_ORG_JUDICIAL_INDEX:
            print("Ожидаемый индекс: " + user_constants.USER_ORG_JUDICIAL_INDEX + "\n"
                  + "Индекс в заказе: " + text)

    # модератор проверяет область юридического адреса
    def moder_check_user_judicial_area(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(4)'))
        assert text == user_constants.USER_ORG_JUDICIAL_AREA
        if text == user_constants.USER_ORG_JUDICIAL_AREA:
            print("Ожидаемая область: " + user_constants.USER_ORG_JUDICIAL_AREA + "\n"
                  + "Область в заказе: " + text)

    # модератор проверяет город юридического адреса
    def moder_check_user_judicial_city(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(5)'))
        assert text == user_constants.USER_ORG_JUDICIAL_CITY
        if text == user_constants.USER_ORG_JUDICIAL_CITY:
            print("Ожидаемый город: " + user_constants.USER_ORG_JUDICIAL_CITY + "\n"
                  + "Город в заказе: " + text)

    # модератор проверяет улицу юридического адреса
    def moder_check_user_judicial_street(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(6)'))
        assert text == user_constants.USER_ORG_JUDICIAL_STREET
        if text == user_constants.USER_ORG_JUDICIAL_STREET:
            print("Ожидаемая улица: " + user_constants.USER_ORG_JUDICIAL_STREET + "\n"
                  + "Улица в заказе: " + text)

    # модератор проверяет дом юридического адреса
    def moder_check_user_judicial_house(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(7)'))
        assert text == user_constants.USER_ORG_JUDICIAL_HOUSE
        if text == user_constants.USER_ORG_JUDICIAL_HOUSE:
            print("Ожидаемый дом: " + user_constants.USER_ORG_JUDICIAL_HOUSE + "\n"
                  + "Дом в заказе: " + text)

    # модератор проверяет офис юридического адреса
    def moder_check_user_judicial_office(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(2) > div > p:nth-child(8)'))
        assert text == user_constants.USER_ORG_JUDICIAL_OFFICE
        if text == user_constants.USER_ORG_JUDICIAL_OFFICE:
            print("Ожидаемый офис: " + user_constants.USER_ORG_JUDICIAL_OFFICE + "\n"
                  + "Офис в заказе: " + text)

    # модератор проверяет индекс фактического адреса
    def moder_check_user_actual_index(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(3)'))
        assert text == user_constants.USER_ORG_ACTUAL_INDEX
        if text == user_constants.USER_ORG_ACTUAL_INDEX:
            print("Ожидаемый индекс: " + user_constants.USER_ORG_ACTUAL_INDEX + "\n"
                  + "Индекс в заказе: " + text)

    # модератор проверяет область фактического адреса
    def moder_check_user_actual_area(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(4)'))
        assert text == user_constants.USER_ORG_ACTUAL_AREA
        if text == user_constants.USER_ORG_ACTUAL_AREA:
            print("Ожидаемая область: " + user_constants.USER_ORG_ACTUAL_AREA + "\n"
                  + "Область в заказе: " + text)

    # модератор проверяет город фактического адреса
    def moder_check_user_actual_city(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(5)'))
        assert text == user_constants.USER_ORG_ACTUAL_CITY
        if text == user_constants.USER_ORG_ACTUAL_CITY:
            print("Ожидаемый город: " + user_constants.USER_ORG_ACTUAL_CITY + "\n"
                  + "Город в заказе: " + text)

    # модератор проверяет улицу фактического адреса
    def moder_check_user_actual_street(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(6)'))
        assert text == user_constants.USER_ORG_ACTUAL_STREET
        if text == user_constants.USER_ORG_ACTUAL_STREET:
            print("Ожидаемая улица: " + user_constants.USER_ORG_ACTUAL_STREET + "\n"
                  + "Улица в заказе: " + text)

    # модератор проверяет дом фактического адреса
    def moder_check_user_actual_house(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(7)'))
        assert text == user_constants.USER_ORG_ACTUAL_HOUSE
        if text == user_constants.USER_ORG_ACTUAL_HOUSE:
            print("Ожидаемый дом: " + user_constants.USER_ORG_ACTUAL_HOUSE + "\n"
                  + "Дом в заказе: " + text)

    # модератор проверяет офис фактического адреса
    def moder_check_user_actual_office(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__organization > div > div > div > div:nth-child(3) > p:nth-child(8)'))
        assert text == user_constants.USER_ORG_ACTUAL_OFFICE
        if text == user_constants.USER_ORG_ACTUAL_OFFICE:
            print("Ожидаемый офис: " + user_constants.USER_ORG_ACTUAL_OFFICE + "\n"
                  + "Офис в заказе: " + text)

    # модератор проверяет ФИО пользователя в заказе
    def moder_check_user_data_fio(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(1) > a'))
        assert text == user_constants.USER_DATA_IN_REQUEST_FIO
        if text == user_constants.USER_DATA_IN_REQUEST_FIO:
            print("Ожидаемое ФИО: " + user_constants.USER_DATA_IN_REQUEST_FIO + "\n"
                  + "ФИО в заказе: " + text)

    # модератор проверяет почту пользователя в заказе
    def moder_check_user_data_mail(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(2) > a'))
        assert text == user_constants.USER_DATA_IN_REQUEST_EMAIL
        if text == user_constants.USER_DATA_IN_REQUEST_EMAIL:
            print("Ожидаемая почта: " + user_constants.USER_DATA_IN_REQUEST_EMAIL + "\n"
                  + "Почта в заказе: " + text)

    # модератор проверяет телефон пользователя в заказе
    def moder_check_user_data_phone(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(3) > a'))
        assert text == user_constants.USER_DATA_IN_REQUEST_PHONE
        if text == user_constants.USER_DATA_IN_REQUEST_PHONE:
            print("Ожидаемый телефон: " + user_constants.USER_DATA_IN_REQUEST_PHONE + "\n"
                  + "Телефон в заказе: " + text)

    # модератор проверяет дату рождения пользователя в заказе
    def moder_check_user_data_birthday(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(4) > p:nth-child(2)'))
        assert text == user_constants.USER_DATA_IN_REQUEST_BIRTHDAY
        if text == user_constants.USER_DATA_IN_REQUEST_BIRTHDAY:
            print("Ожидаемая дата: " + user_constants.USER_DATA_IN_REQUEST_BIRTHDAY + "\n"
                  + "Дата в заказе: " + text)

    # модератор проверяет адрес пользователя в заказе
    def moder_check_user_data_address(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(5) > p:nth-child(2)'))
        assert text == user_constants.USER_DATA_IN_REQUEST_ADDRESS
        if text == user_constants.USER_DATA_IN_REQUEST_ADDRESS:
            print("Ожидаемый адрес: " + user_constants.USER_DATA_IN_REQUEST_ADDRESS + "\n"
                  + "Адрес в заказе: " + text)

    # модератор проверяет текущую организацию пользователя в заказе
    def moder_check_user_data_org_name(self):
        text = BasePage.get_text(self, (By.CSS_SELECTOR,
                                        '#app > div.page > div > div:nth-child(2) > div.pre-moderation > div > div.pre-moderation__user > div > div > div:nth-child(6) > a'))
        assert text == user_constants.USER_DATA_IN_REQUEST_ORG_ACTUAL_NAME
        if text == user_constants.USER_DATA_IN_REQUEST_ORG_ACTUAL_NAME:
            print("Ожидаемая организация: " + user_constants.USER_DATA_IN_REQUEST_ORG_ACTUAL_NAME + "\n"
                  + "Организация в заказе: " + text)
