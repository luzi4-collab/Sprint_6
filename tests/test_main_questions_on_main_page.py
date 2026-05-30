# импорт библиотек
import pytest
from pages.main_page import MainPageScooter
from locators.main_page_locators import *
from data import *
import allure

# класс с автотестом
class TestMainQuestions:

    @pytest.mark.parametrize(
        "question_button, question_answer, answer_text",
        [
            (MAIN_QUESTION_ONE, MAIN_QUESTION_ONE_ANSWER, answer_text_1),
            (MAIN_QUESTION_TWO, MAIN_QUESTION_TWO_ANSWER, answer_text_2),
            (MAIN_QUESTION_THREE, MAIN_QUESTION_THREE_ANSWER, answer_text_3),
            (MAIN_QUESTION_FOUR, MAIN_QUESTION_FOUR_ANSWER, answer_text_4),
            (MAIN_QUESTION_FIVE, MAIN_QUESTION_FIVE_ANSWER, answer_text_5),
            (MAIN_QUESTION_SIX, MAIN_QUESTION_SIX_ANSWER, answer_text_6),
            (MAIN_QUESTION_SEVEN, MAIN_QUESTION_SEVEN_ANSWER, answer_text_7),
            (MAIN_QUESTION_EIGHT, MAIN_QUESTION_EIGHT_ANSWER, answer_text_8)
        ]
    )

    @allure.title('Проверка вопроса')
    def test_check_main_question_one_answer(self, driver,question_button,question_answer, answer_text):
        # создали объект класса главной страницы
        main_page = MainPageScooter(driver)
        # открываем главную страницу
        main_page.open_main_page()
        # открываем вопрос
        main_page.open_question(question_button)
        # сравниваем полученный и ожидаемый тексты
        assert main_page.get_text(question_answer) == answer_text
