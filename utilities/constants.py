from datetime import datetime, timedelta


class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_URL = 'https://dzen.ru/'


class OrderData:
    TOMORROW = (datetime.now() + timedelta(days=1)).strftime('%d-%m-%Y')

    FIRST_ORDER = {
        'name': 'Иван',
        'surname': 'Петров',
        'address': 'ул. Примерная, 1',
        'metro': 'Черкизовская',
        'phone': '89991234567',
        'date': TOMORROW,
        'rental_period': 'сутки',
        'color': 'black',
        'comment': 'Тестовый заказ'
    }

    SECOND_ORDER = {
        'name': 'Мария',
        'surname': 'Сидорова',
        'address': 'пр. Тестовый, 15',
        'metro': 'Красные Ворота',
        'phone': '89997654321',
        'date': TOMORROW,
        'rental_period': 'трое суток',
        'color': 'grey',
        'comment': 'Второй тестовый заказ'
    }