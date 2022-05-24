import time
import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'], scope='class')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(
            executable_path=r'C:\ru.estate.prod.autotests\resources\chromedriver.exe')
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield driver
        time.sleep(1)
        driver.close()
        driver.quit()
    if request.param == 'firefox':
        driver = webdriver.Firefox(
            executable_path=r'C:\ru.estate.prod.autotests\resources\geckodriver.exe')
        driver.implicitly_wait(30)
        # driver.maximize_window()
        yield driver
        time.sleep(1)
        driver.close()
        driver.quit()


@pytest.fixture(params=['chrome'], scope='function')
def func_scope():
    driver.implicity_wait(30)
