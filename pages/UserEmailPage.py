from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class UserEmailPage(BasePage):
    # Метод авторизует пользователя в почту на мейл ру
    def open_email_site_and_authorize(self):
        # пользователь заходит на сайт
        BasePage.open_site(self, "https://mail.ru/")

        # пользователь вводит имя аккаунта
        BasePage.send_keys(self, (By.XPATH, '//*[@data-testid="login-input"]'), '01.01.test')
        # пользователь нажимает кнопку ввести пароль
        BasePage.click(self, (By.XPATH, '//*[@data-testid="enter-password"]'))
        # пользователь вводит пароль
        BasePage.send_keys(self, (By.XPATH, '//*[@data-testid="password-input"]'), 'Ao3EFT1rorp%')
        # пользователь нажимает кнопку войти
        BasePage.click(self, (By.XPATH, '//*[@data-testid="login-to-mail"]'))
        # тут вылезает предупреждение, нажимаем ПРОДОЛЖИТЬ
        BasePage.click(self, (By.XPATH, '//*[@id="content"]/div/div/div/p/a'))

    # пользователь кликает по приветственному письму
    def click_on_welcome_letter(self):
        BasePage.click(self, (By.XPATH, '//*[@class="ll-sj__normal" and text()="Welcome to MTS Estate"]'))

    # пользователь проверяет заголовок приветственного письма
    def check_letter_title(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="thread__subject"]'))
        assert text == 'Welcome to MTS Estate'
        if text == 'Welcome to MTS Estate':
            print('Заголовок письма верный')

    # пользователь проверяет текст приветственного письма
    def check_letter_inner_greeting_text(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="letter__body"]'))
        one_line = text.replace("\n", " ")
        assert one_line == 'Здравствуйте, Дмитрий!' \
                           '  Благодарим Вас за выбор сервиса МТС Estate.  С уважением, команда МТС Estate'
        if one_line == 'Здравствуйте, Дмитрий!' \
                       '  Благодарим Вас за выбор сервиса МТС Estate.  С уважением, команда МТС Estate':
            print('Текст письма верный')

    # пользователь кликает по письму сообщающем, что его обращение через форму обратной связи зарегистрировано
    def user_click_letter_appeal_trough_the_form_is_registered(self):
        BasePage.click(self, (By.XPATH, '//*[@class="ll-sj__normal"  and text()="MTS Estate. Спасибо за обращение."]'))

    # пользователь проверяет заголовок письма,
    # сообщающего, что его обращение через форму обратной связи зарегистрировано
    def user_check_title_letter_appeal_trough_the_form_is_registered(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="thread__subject"]'))
        assert text == 'MTS Estate. Спасибо за обращение.'
        if text == 'MTS Estate. Спасибо за обращение.':
            print('Заголовок письма верный')

    # пользователь проверяет текст письма сообщающего, что его обращение через форму обратной связи зарегистрировано
    def user_check_text_letter_appeal_trough_the_form_is_registered(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[@class="letter__body"]'))
        one_line = text.replace("\n", " ")
        assert one_line == 'Благодарим Вас за обращение.' \
                           ' В ближайшее время мы рассмотрим Ваш комментарий и при необходимости свяжемся с Вами.' \
                           ' С уважением, команда МТС Estate!'
        if one_line == 'Благодарим Вас за обращение.' \
                       ' В ближайшее время мы рассмотрим Ваш комментарий и при необходимости свяжемся с Вами.' \
                       ' С уважением, команда МТС Estate!':
            print('Текст письма верен')

    # пользователь выбирает письмо с текстом шаблона 1
    def user_select_letter_pattern_1_in_email_box(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="ll-sj__normal" and text()="МТС Estate. Итоги предварительной модерации"]'))

    # пользователь проверяет текст ответа из шаблона 1
    def check_letter_pattern_1_in_email_box(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[text()="текст письма 1"]'))
        assert text == 'текст письма 1'
        if text == 'текст письма 1':
            print('Шаблон ответа модератора №1 получен пользователем')

    # пользователь выбирает письмо с текстом шаблона 2
    def user_select_letter_pattern_2_in_email_box(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="ll-sj__normal" and text()="МТС Estate. Итоги предварительной модерации"]'))

    # пользователь проверяет текст ответа из шаблона 2
    def check_letter_pattern_2_in_email_box(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[text()="текст письма 2"]'))
        assert text == 'текст письма 2'
        if text == 'текст письма 2':
            print('Шаблон ответа модератора №2 получен пользователем')

    # пользователь выбирает письмо с текстом шаблона 3
    def user_select_letter_pattern_3_in_email_box(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="ll-sj__normal" and text()="МТС Estate. Итоги предварительной модерации"]'))

    # пользователь проверяет текст ответа из шаблона 3
    def check_letter_pattern_3_in_email_box(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[text()="текст письма 3"]'))
        assert text == 'текст письма 3'
        if text == 'текст письма 3':
            print('Шаблон ответа модератора №3 получен пользователем')

    # пользователь выбирает письмо с текстом шаблона 4
    def user_select_letter_pattern_4_in_email_box(self):
        BasePage.click(self, (
            By.XPATH, '//*[@class="ll-sj__normal" and text()="МТС Estate. Итоги предварительной модерации"]'))

    # пользователь проверяет текст ответа из шаблона 4
    def check_letter_pattern_4_in_email_box(self):
        text = BasePage.get_text(self, (By.XPATH, '//*[text()="текст письма 4"]'))
        assert text == 'текст письма 4'
        if text == 'текст письма 4':
            print('Шаблон ответа модератора №4 получен пользователем')
