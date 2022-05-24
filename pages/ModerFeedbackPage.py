from selenium.webdriver.common.by import By

from constants import moder_constants
from pages.BasePage import BasePage


class ModerFeedbackPage(BasePage):
    # модератор авторизуется
    def login(self):
        BasePage.moder_auth(self)

    # переход на страницу "обратная связь" страница модератора
    def open_reverse_connections_page(self):
        BasePage.open_site(self, moder_constants.MODER_REVERSE_CONNECTION_PAGE)

    # МОДЕРАТОР проверяет имя в карточке письма
    def check_name_in_letter_card(self):
        text = BasePage.get_text(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/div/p'))
        assert text == 'TEST'
        if text == 'TEST':
            print('Имя, в карточке письма, отображается и верно')

    # МОДЕРАТОР проверяет номер телефона в карточке письма
    def check_phone_in_letter_card(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="cell" and text()="+7 (123) 456-78-90"]'))
        assert text == '+7 (123) 456-78-90'
        if text == '+7 (123) 456-78-90':
            print('Телефон, в карточке письма, отображается и верен')

    # МОДЕРАТОР проверяет почту в карточке письма
    def check_mail_in_letter_card(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@href="mailto:01.01.test@mail.ru"]'))
        assert text == '01.01.test@mail.ru'
        if text == '01.01.test@mail.ru':
            print('Почта, в карточке письма, отображается и верна')

    # МОДЕРАТОР проверяет сообщение в карточке письма
    def check_message_in_letter_card(self):
        self.driver.maximize_window()
        text = BasePage.get_text(self, (
            By.XPATH,
            '//*[@id="app"]/div[1]/div/div/div/div/main/div[1]/div/div/div[3]/table/tbody/tr[1]/td[5]/div/div/p'))
        assert text == 'TEST Message'
        if text == 'TEST Message':
            print('Сообщение, в карточке письма, отображается и верно')

    # МОДЕРАТОР нажимает кнопку подробнее
    def click_btn_more_details(self):
        BasePage.click(self, (By.XPATH, '//*[1][@class="el-button el-button--primary el-button--mini"]'))

    # МОДЕРАТОР проверяет, что появилась модалка с заголовком "сообщение пользователя"
    def check_modal_window_title(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="el-dialog__title" and text()="Сообщение пользователя"]'))
        assert text == 'Сообщение пользователя'
        if text == 'Сообщение пользователя':
            print('Заголовок, в модальном окне, отображается и верен')

    # МОДЕРАТОР нажимает крестик в модалке(проверка, что окно можно закрыть)
    def click_cross_in_modal_window(self):
        BasePage.click(self, (By.XPATH, '//*[@class="el-dialog__headerbtn"]'))

    # МОДЕРАТОР проверяет заголовок имя пользователя в модальном окне
    def check_title_of_name_in_modal_window(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="content-item__label" and text()="Имя пользователя:"]'))
        assert text == 'Имя пользователя:'
        if text == 'Имя пользователя:':
            print('Заголовок для имени, в модальном окне, верный')

    # МОДЕРАТОР проверяет имя в модальном окне
    def check_name_in_modal_window(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="content-item__value" and text()="TEST"]'))
        assert text == 'TEST'
        if text == 'TEST':
            print('Имя, в модальном окне, отображается и верно')

    # МОДЕРАТОР проверяет заголовок почты в модальном окне
    def check_title_of_mail_in_modal_window(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/div/p[1]'))
        assert text == 'E-mail:'
        if text == 'E-mail:':
            print('Заголовок для поля почты, в модальном окне, верный')

    # МОДЕРАТОР проверяет почту в модальном окне
    def check_mail_in_modal_window(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/div/p[2]'))
        assert text == '01.01.test@mail.ru'
        if text == '01.01.test@mail.ru':
            print('Почта, в модальном окне, отображается и верна')

    # МОДЕРАТОР проверяет заголовок телефона в модальном окне
    def check_title_of_phone_in_modal_window(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div[4]/div/p[1]'))
        assert text == 'Телефон:'
        if text == 'Телефон:':
            print('Заголовок для поля телефон, в модальном окне, верный')

    # МОДЕРАТОР проверяет номер телефона в модальном окне
    def check_phone_in_modal_window(self):
        text = BasePage.get_text(self, (
            By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div[4]/div/p[2]'))
        assert text == '+7 (123) 456-78-90'
        if text == '+7 (123) 456-78-90':
            print('Телефон, в модальном окне, отображается и верен')

    # МОДЕРАТОР проверяет заголовок сообщения в модальном окне
    def check_title_of_message_in_modal_window(self):
        text = BasePage.get_text(self,
                                 (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/p[1]'))
        assert text == 'Сообщение:'
        if text == 'Сообщение:':
            print('Заголовок для поля сообщения, в модальном окне, верный')

    # МОДЕРАТОР проверяет сообщение в модальном окне
    def check_message_in_modal_window(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="content-item__value" and text()="TEST Message"]'))
        assert text == 'TEST Message'
        if text == 'TEST Message':
            print('Сообщение, в модальном окне, отображается и верно')

    # МОДЕРАТОР нажимает кнопку "обработать"
    def click_btn_process(self):
        BasePage.click(self, (By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/div/div/div[3]/div/button'))

    # МОДЕРАТОР проверяет, что кнопка "обработать" для данного письма не активна
    def check_btn_process_is_disabled(self):
        element = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div/div/div/div[3]/div/button')
        element_attribute = element.get_attribute('disabled')
        assert element_attribute == 'true'
        if element_attribute == 'true':
            print('Письмо обработано')
