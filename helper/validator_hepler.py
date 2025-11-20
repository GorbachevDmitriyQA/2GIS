"""Помощник для проверок"""
class AssertionHelper:
    default_error_message = "Значение не совпадает с ожидаемым"


    @staticmethod
    def are_equals(actual, expected):
        assert actual == expected, \
            (f"Значение не совпадает с ожидаемым\r "
             f"Текущее значение = {actual}\r"
             f" Ожидаемое значение = {expected}")