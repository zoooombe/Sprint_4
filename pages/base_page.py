import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть страницу")
    def open(self):
        try:
            self.driver.get(self.base_url)
            self.accept_cookies()
        except WebDriverException as e:
            logger.error(f"Ошибка при открытии страницы: {e}")
            raise

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except (TimeoutException, WebDriverException):
            logger.info("Кнопка принятия куки не найдена")

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except WebDriverException as e:
            logger.error(f"Ошибка при скролле к элементу: {e}")
            raise

    @allure.step("Дождаться видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент не найден: {locator}")
            raise

    @allure.step("Дождаться кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Элемент не кликабелен: {locator}")
            raise

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            self.scroll_to_element(element)
            element.click()
        except WebDriverException as e:
            logger.error(f"Ошибка при клике на элемент: {e}")
            try:
                self.driver.execute_script("arguments[0].click();", element)
            except:
                raise

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, main_window, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                break

        return True

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, url_part, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )