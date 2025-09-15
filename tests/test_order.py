import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utilities.constants import OrderData, Urls


class TestOrder:
    @pytest.mark.parametrize('order_data', [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER])
    @allure.title('Тест заказа самоката через верхнюю кнопку')
    def test_order_flow_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.fill_customer_info(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro'],
            order_data['phone']
        )

        order_page.fill_rent_info(
            order_data['date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @pytest.mark.parametrize('order_data', [OrderData.FIRST_ORDER, OrderData.SECOND_ORDER])
    @allure.title('Тест заказа самоката через нижнюю кнопку')
    def test_order_flow_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_customer_info(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro'],
            order_data['phone']
        )

        order_page.fill_rent_info(
            order_data['date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

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

        main_window = main_page.get_current_window_handle()

        main_page.click_yandex_logo()

        main_page.switch_to_new_window(main_window)

        main_page.wait_for_page_load("dzen.ru")

        assert "dzen.ru" in driver.current_url