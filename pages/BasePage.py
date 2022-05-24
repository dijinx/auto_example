import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import user_constants, moder_constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # перейти на страницу
    def open_site(self, url):
        self.driver.get(url)

    # кликнуть по  видимому элементу
    def click(self, by_locator):
        WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(by_locator)).click()

    # очистить поле и внести текст
    def send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(by_locator))
        element.click()
        element.clear()
        element.send_keys(text)

    # не очищать поле и внести текст
    def send_keys_without_clear(self, by_locator, text):
        element = WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(by_locator))
        element.click()
        element.send_keys(text)

    # загрузить файл
    def load_file(self, by_locator, text):
        element = WebDriverWait(self.driver, 90).until(EC.invisibility_of_element_located(by_locator))
        element.send_keys(text)

    # получить текст элемента
    def get_text(self, by_locator):
        text = WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(by_locator))
        return text.text

    # проверить видимость элемента
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # получить имя страницы
    def get_title(self, title):
        element = WebDriverWait(self.driver, 90).until(EC.title_is(title))
        return element

    # получить текущую ссылку и проверить с эталоном
    def check_url(self, url):
        WebDriverWait(self.driver, 90).until(EC.url_to_be(url))

    # получить адрес текущей страницы
    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    # прокрутить до видимости элемента в окне браузера
    def scroll_into_view(self, script, by_locator):
        self.driver.execute_script(script, by_locator)

    # запустить скрипт в консоли браузера
    def run_js_script(self, script):
        self.driver.execute_script(script)

    # очистить поле ввода
    def clear_input(self, by_locator):
        self.driver.find_element(by_locator).clear()

    # авторизация пользователя с полностью заполненным профилем
    def user_auth(self):
        self.driver.get(user_constants.USER_PROD_AUTHORIZATION_PAGE)
        self.driver.find_element(By.ID, 'phoneInput').send_keys(user_constants.USER_AUTHORIZATION_PHONE_NUMBER)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(user_constants.USER_AUTHORIZATION_PASSWORD)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()

    # авторизация пользователя для заполнения организации
    def user_auth_new_user(self):
        self.driver.get(user_constants.USER_PROD_AUTHORIZATION_PAGE)
        self.driver.find_element(By.ID, 'phoneInput').send_keys(user_constants.USER_REGISTRATION_PHONE_NUMBER)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(user_constants.USER_REGISTRATION_PASSWORD)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()

    # авторизация пользователя
    def user_authorization(self, login, password):
        self.driver.get(user_constants.USER_PROD_AUTHORIZATION_PAGE)
        self.driver.find_element(By.ID, 'phoneInput').send_keys(login)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()

    # авторизация пользователя для заполнения профиля,платёжных реквизитов
    def user_auth_new_user_for_profile_and_requisites(self):
        self.driver.get(user_constants.USER_PROD_AUTHORIZATION_PAGE)
        self.driver.find_element(By.ID, 'phoneInput').send_keys(
            user_constants.USER_PROFILE_AND_REQUISITES_REGISTRATION_PHONE_NUMBER)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(
            user_constants.USER_PROFILE_AND_REQUISITES_REGISTRATION_PASSWORD)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()

    # авторизация модератора
    def moder_auth(self):
        self.driver.get(moder_constants.MODER_PROD_MAIN_PAGE)
        self.driver.find_element(By.ID, 'phoneInput').send_keys(moder_constants.MODER_AUTHORIZATION_PHONE_NUMBER)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(moder_constants.MODER_AUTHORIZATION_PASSWORD)
        self.driver.find_element(By.CLASS_NAME, 'button__content').click()

    # пользователь создаёт заказ - загружен рыночный отчёт и обе ЭЦП, отправляет модератору
    # необходим зарегистрированный пользователь
    def user_create_request(self):
        BasePage.user_auth(self)
        time.sleep(3)
        self.driver.get(user_constants.USER_PROD_FAVORITES_PAGE)
        self.driver.find_element(By.ID, 'search-input').send_keys(user_constants.USER_CADASTRAL_NUMBER_0)
        time.sleep(5)
        self.driver.find_element(By.ID, 'search-btn').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@data-test-id="add-to-cart-button"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="profile-widget-cart"]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@class="el-button cart__actions-btn el-button--primary el-button--small"]').click()

        self.driver.find_element(By.XPATH, '//input[@accept="application/pdf, .zip, .rar"]').send_keys(
            user_constants.USER_MARKET_PRICE_REPORT_FILE)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@accept=".sig"]').send_keys(user_constants.USER_SIGN_1_FILE)
        self.driver.find_element(By.XPATH, '//*[@accept=".sig"]').send_keys(user_constants.USER_SIGN_2_FILE)
        self.driver.find_element(By.XPATH,
                                 '//*[@class="el-button page-order__next-step-btn el-button--primary el-button--small"]').click()
