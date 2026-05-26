import allure
from url import MAIN_URL
from pages.base_page import BasePageScooter
from locators.main_page_locators import *

class MainPageScooter(BasePageScooter):
    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_page(MAIN_URL)
    
    @allure.step('Открыть вопрос')
    def open_question(self, locator):
        self.scroll_to_point(locator)
        self.click(locator)

    @allure.step('Получаем текст ответа на вопрос')
    def get_text(self, locator):
        return self.wait_visible(locator).text
    
    @allure.step('Ожидаем видимости кнопки Заказать')
    def visibility_of_order_button(self):
        self.wait_visible(ORDER_BUTTON_HEADER)

    @allure.step('Получаем текущий url')
    def get_main_page_url(self):
        self.get_current_url()

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self, locator):
        self.scroll_to_point(locator)
        self.click(locator)
