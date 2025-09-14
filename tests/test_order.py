import pytest
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utilities.constants import OrderData, Urls


class TestOrder:
    @pytest.mark.parametrize('order_button', ['top', 'bottom'])
    @pytest.mark.parametrize('order_data', [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER])
    @allure.title('Тест заказа самоката через кнопку "{order_button}"')
    def test_order_flow(self, driver, order_button, order_data):
        main_page = MainPage(driver)
        main_page.open()

        if order_button == 'top':
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)

        time.sleep(2)

        order_page.fill_customer_info(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro'],
            order_data['phone']
        )

        time.sleep(2)

        order_page.fill_rent_info(
            order_data['date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )

        time.sleep(3)

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message, f"Сообщение об успехе не содержит ожидаемый текст: {success_message}"

    @allure.title('Тест редиректа на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert driver.current_url == Urls.BASE_URL

    @allure.title('Тест редиректа на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_window = driver.current_window_handle

        main_page.click_yandex_logo()

        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)

        for window_handle in driver.window_handles:
            if window_handle != main_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 15).until(
            lambda d: "dzen.ru" in d.current_url
        )

        assert "dzen.ru" in driver.current_url