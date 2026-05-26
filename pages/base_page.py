from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10

class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=20)

    def open_page(self, url):
        self.driver.get(url)

    # Ожидаем видимости локатора
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Прокручиваем до элемента
    def scroll_to_point(self, locator):
        el = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
    # Клик по локатору
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_current_url(self) -> str: 
        return self.driver.current_url
    
    # Перейти на новую вкладку
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    # Дождаться появления значения в url
    def wait_url_contains(self, text: str):
        self.wait.until(EC.url_contains(text))

    def input_text(self, locator, text):
        element = self.wait_visible(locator)
        element.send_keys(text)

    # Дождаться появления локатора
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
