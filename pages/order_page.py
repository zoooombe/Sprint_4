from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.CLASS_NAME, "select-search__input")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//button/div[text()='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[text()='{}']")
    COLOR_CHECKBOX = (By.ID, "{}")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def fill_customer_info(self, name, surname, address, metro, phone):
        self.wait_for_element(self.NAME_INPUT, timeout=15).send_keys(name)
        self.wait_for_element(self.SURNAME_INPUT, timeout=15).send_keys(surname)
        self.wait_for_element(self.ADDRESS_INPUT, timeout=15).send_keys(address)

        metro_dropdown = self.wait_for_clickable(self.METRO_STATION_DROPDOWN, timeout=15)
        metro_dropdown.click()
        metro_option = self.wait_for_clickable(
            (self.METRO_STATION_OPTION[0], self.METRO_STATION_OPTION[1].format(metro)),
            timeout=15
        )
        metro_option.click()

        self.wait_for_element(self.PHONE_INPUT, timeout=15).send_keys(phone)

        next_button = self.wait_for_clickable(self.NEXT_BUTTON, timeout=15)
        self.driver.execute_script("arguments[0].click();", next_button)

        self.wait_for_element(self.DATE_INPUT, timeout=15)

    def fill_rent_info(self, date, period, color, comment):
        date_input = self.wait_for_element(self.DATE_INPUT, timeout=15)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)

        date_input.send_keys(Keys.ENTER)

        period_dropdown = self.wait_for_clickable(self.RENTAL_PERIOD_DROPDOWN, timeout=15)
        period_dropdown.click()

        period_option = self.wait_for_clickable(
            (self.RENTAL_PERIOD_OPTION[0], self.RENTAL_PERIOD_OPTION[1].format(period)),
            timeout=15
        )
        period_option.click()

        color_locator = (self.COLOR_CHECKBOX[0], self.COLOR_CHECKBOX[1].format(color))
        color_checkbox = self.wait_for_clickable(color_locator, timeout=15)
        color_checkbox.click()

        self.wait_for_element(self.COMMENT_INPUT, timeout=15).send_keys(comment)

        order_button = self.wait_for_clickable(self.ORDER_BUTTON, timeout=15)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)

        import time
        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", order_button)

        confirm_button = self.wait_for_clickable(self.CONFIRM_BUTTON, timeout=15)
        self.driver.execute_script("arguments[0].click();", confirm_button)

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE, timeout=15).text