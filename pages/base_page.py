from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        try:
            self.driver.get(self.base_url)
            self.accept_cookies()
        except WebDriverException as e:
            print(f"Ошибка при открытии страницы: {e}")
            raise

    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except (TimeoutException, WebDriverException):
            pass

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except WebDriverException as e:
            print(f"Ошибка при скролле к элементу: {e}")
            raise

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Элемент не найден: {locator}")
            raise

    def wait_for_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Элемент не кликабелен: {locator}")
            raise

    def click_element(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            self.scroll_to_element(element)
            element.click()
        except WebDriverException as e:
            print(f"Ошибка при клике на элемент: {e}")
            try:
                self.driver.execute_script("arguments[0].click();", element)
            except:
                raise