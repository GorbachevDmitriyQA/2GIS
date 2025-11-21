"""Помощник для проверок"""
class AssertionHelper:
    """
    Класс-помощник для выполнения проверок

    Предоставляет:
    - универсальный метод проверки двух значений на равенство
    - универсальный метод проверки статус кода ответа от сервера
    """
    default_error_message = "значение не совпадает с ожидаемым"
    @staticmethod
    def are_equals(actual, expected):
        assert actual == expected, \
            (f"Значение не совпадает с ожидаемым\r "
             f"Текущее значение = {actual}\r"
             f" Ожидаемое значение = {expected}")
    @staticmethod
    def check_status_code(actual_status_code, expected_status_code):
        assert actual_status_code == expected_status_code, \
            (f"Статус код ответа от сервера не совпадает с ожидаемым\r "
             f"Текущий status code = {actual_status_code}\r"
             f"Ожидаемый status code = {expected_status_code}")