# импорт библиотек
from pages.main_page import MainPageScooter
from locators.main_page_locators import *
from pages.order_page import *
from data import *
import allure

# класс с автотестом
class TestLogoes:

    @allure.title('Проверка перехода на главную страницу по клику на САМОКАТ')
    def test_check_transport_by_logo_scooter(self, driver):
        # создали объект класса страницы заказа
        order_page = OrderPageScooter(driver)
        # открываем страницу заказа
        order_page.open_order_page()
        # клик по САМОКАТ
        order_page.click_logo_scooter()
        # создали объект класса главной страницы
        main_page = MainPageScooter(driver)
        # ожидаем появления кнопки Заказать в хедере главной страницы
        main_page.visibility_of_order_button()
        # сравниваем полученный и ожидаемый url
        assert main_page.get_current_url() == MAIN_URL

    @allure.title('Проверка перехода на главную страницу по клику на ЯНДЕКС')
    def test_check_transport_by_logo_yandex(self, driver):
        # создали объект класса страницы заказа
        order_page = OrderPageScooter(driver)
        # открываем страницу заказа
        order_page.open_order_page()
        # клик по ЯНДЕКС
        order_page.click_logo_yandex()
        # ждём загрузки дзена во второй вкладке браузера
        order_page.wait_dzen_opened_in_new_tab()
        # сравниваем полученный и ожидаемый url
        assert DZEN_URL_PART in order_page.get_order_page_url()
