from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import *
from locators.order_page_locators import *
from url import *
import allure

class OrderPageScooter(BasePageScooter):
    
    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.open_page(ORDER_URL)

    @allure.step('Клик по САМОКАТ')
    def click_logo_scooter(self):
        self.click(LOGO_SCOOTER)

    @allure.step('Клик по ЯНДЕКС')
    def click_logo_yandex(self):
        self.click(YANDEX_LOGO)

    @allure.step("Проверить, что Дзен открылся в новой вкладке")
    def wait_dzen_opened_in_new_tab(self):
        self.switch_to_new_tab()
        self.wait_url_contains(DZEN_URL_PART)

    @allure.step('Получаем текущий url')
    def get_order_page_url(self):
        return self.get_current_url()
    
    @allure.step('Ввести текст в поле Имя')
    def input_text_into_name(self, text):
        self.input_text(INPUT_NAME, text)

    @allure.step('Ввести текст в поле Фамилия')
    def input_text_into_surname(self, text):
        self.input_text(INPUT_SURNAME, text)

    @allure.step('Ввести текст в поле Адрес')
    def input_text_into_address(self, text):
        self.input_text(INPUT_ADDRESS, text)

    @allure.step('Ввести текст в поле Метро и выбрать его')
    def input_text_into_metro(self, text):
        self.click(INPUT_METRO_STATION)
        self.input_text(INPUT_METRO_STATION, text)
        self.wait_visible(INPUT_METRO_STATION).send_keys(Keys.ARROW_DOWN)
        self.wait_visible(INPUT_METRO_STATION).send_keys(Keys.ENTER)

    @allure.step('Ввести номер телефона')
    def input_text_into_phone(self, text):
        self.input_text(INPUT_PHONE, text)

    @allure.step('Выбрать дату')
    def input_text_into_date(self, text):
        self.input_text(INPUT_DATE, text)
        self.wait_visible(INPUT_DATE).send_keys(Keys.ENTER)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self, period_text: str):
        self.click(RENT_PERIOD_DROPDOWN)
        period = (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space()='{period_text}']")
        self.click(period)

    @allure.step('Выбрать цвет')
    def click_colour_checkbox(self, colour):
        self.click(colour)

    @allure.step('Ввести текст в поле Комментарий')
    def input_text_into_comment(self, text):
        self.input_text(INPUT_COMMENT, text)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.click(NEXT_BUTTON)

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.click(ORDER_BUTTON)

    @allure.step('Нажать кнопку Да')
    def click_yes_button(self):
        self.click(YES_BUTTON)

    @allure.step("Дождаться появления кнопки 'Посмотреть статус'")
    def wait_view_status_button(self):
        return self.wait_clickable(VIEW_STATUS_BUTTON)
     