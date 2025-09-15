import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы для вопросов
    QUESTION_LOCATOR = (By.CSS_SELECTOR, "[id^='accordion__heading-']")
    ANSWER_LOCATOR = (By.CSS_SELECTOR, "[id^='accordion__panel-']")

    # Локаторы для кнопок заказа
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")

    # Локаторы для логотипов
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    @allure.step("Кликнуть на вопрос")
    def click_question(self, index):
        question_locator = (By.ID, f"accordion__heading-{index}")
        self.click_element(question_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        answer = self.wait_for_element((By.ID, f"accordion__panel-{index}"))
        return answer.text

    @allure.step("Кликнуть на верхнюю кнопку заказа")
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        # Прокручиваем к нижней кнопке заказа
        button = self.wait_for_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)

        # Ждем, пока кнопка станет полностью видимой и кликабельной
        self.wait_for_clickable(self.ORDER_BUTTON_BOTTOM, timeout=5)

        # Кликаем с помощью JavaScript для избежания проблем с перекрытием
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Получить идентификатор текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle