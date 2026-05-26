from selenium.webdriver.common.by import By

INPUT_NAME = [By.XPATH, ".//input[@placeholder='* Имя']"]
INPUT_SURNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
INPUT_ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
INPUT_PHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Заказать']")
INPUT_METRO_STATION = [By.XPATH, ".//input[@class='select-search__input']"]
LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
BLACK_COLOUR_CHECKBOX = (By.XPATH, "//label[@for='black']")
GREY_COLOUR_CHECKBOX = (By.XPATH, "//label[@for='grey']")
NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")
INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space()='Да']")
VIEW_STATUS_BUTTON = (By.XPATH, "//button[normalize-space()='Посмотреть статус']")
