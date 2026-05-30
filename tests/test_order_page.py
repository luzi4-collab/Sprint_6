# импорт библиотек
import pytest
from pages.order_page import OrderPageScooter
from pages.main_page import MainPageScooter
from pages.main_page import ORDER_BUTTON_HEADER, ORDER_BUTTON_FINISH
from locators.order_page_locators import *
from data import *
import allure

# класс с автотестом
class TestOrderSucsess:

    @pytest.mark.parametrize(
        "button, name, surname, address, metro_station, phone, date, period, colour, comment",
        [
            (ORDER_BUTTON_HEADER, name_1, surname_1, address_1, metro_1, phone_1, date_1, period_1, BLACK_COLOUR_CHECKBOX, comment_1),
            (ORDER_BUTTON_FINISH, name_2, surname_2, address_2, metro_2, phone_2, date_2, period_2, GREY_COLOUR_CHECKBOX, comment_2)
        ]
    )

    @allure.title('Успешный заказ самоката')
    def test_order_succsess(self, driver, button, name, surname, address, metro_station, phone, date, period, colour, comment):
        # создали объект класса главной страницы
        main_page = MainPageScooter(driver)
        # открываем главную страницу
        main_page.open_main_page()
        # нажимаем кнопку Заказать
        main_page.click_order_button(button)
        # создали объект класса страницы заказа
        order_page = OrderPageScooter(driver)
        # заполнение полей
        order_page.input_text_into_name(name)
        order_page.input_text_into_surname(surname)
        order_page.input_text_into_address(address)
        order_page.input_text_into_metro(metro_station)
        order_page.input_text_into_phone(phone)
        order_page.click_next_button()
        order_page.input_text_into_date(date)
        order_page.choose_rent_period(period)
        order_page.click_colour_checkbox(colour)
        order_page.input_text_into_comment(comment)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.wait_view_status_button().is_displayed()
        