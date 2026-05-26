# фикстуры для тестов

# импорт библиотек (модулей)
import pytest
from selenium import webdriver

# старт и завершение работы браузера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
