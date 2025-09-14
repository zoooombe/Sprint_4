from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR = (By.ID, "accordion__panel-{}")

    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH,
                           "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[last()]")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def click_question(self, index):
        question_locator = (self.QUESTION_LOCATOR[0], self.QUESTION_LOCATOR[1].format(index))
        self.click_element(question_locator)

    def get_answer_text(self, index):
        answer = self.wait_for_element((self.ANSWER_LOCATOR[0], self.ANSWER_LOCATOR[1].format(index)))
        return answer.text

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        button = self.wait_for_element(self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        import time
        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", button)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)