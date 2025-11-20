from contextlib import nullcontext
from datetime import datetime
import allure
from helper.validator_hepler import AssertionHelper
class ApiFavoriteValidator:


    @allure.step("Проверка ответа при создании избранного места")
    def check_success_favorite_create_response(self, response, expected_data):
        assert response.status_code == 200, f"Статус код ответа {AssertionHelper.default_error_message}"
        json_data = response.json()
        created_date = json_data["created_at"]
        assert isinstance(json_data["id"], int),\
            f"id в ответе {AssertionHelper.default_error_message} типом значения integer"
        assert json_data["title"] == expected_data["title"], f"title {AssertionHelper.default_error_message}"
        assert json_data["lat"] == expected_data["lat"], f"lat {AssertionHelper.default_error_message}"
        assert json_data["lon"] == expected_data["lon"], f"lon {AssertionHelper.default_error_message}"
        if expected_data.get("color") is not None:
            assert json_data["color"] == expected_data["color"], f"color {AssertionHelper.default_error_message}"
        else: assert json_data["color"] is None, f"color значение по умолчанию (null) {AssertionHelper.default_error_message}"
        self.check_created_at_value(created_date)
        return ApiFavoriteValidator

    @allure.step("Проверка формата даты в ответе от сервера")
    def check_created_at_value(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            assert False, "Дата не соответствует формату YYYY-MM-DDThh:mm:ss±hh:mm"
        return ApiFavoriteValidator


    @allure.step("Проверка сообщения об отсутствии токена")
    def check_unauthorized_error_response(self, response):
        assert response.status_code == 401, "Статус код ответа не совпадает с ожидаемым"
        assert response.json()["error"]["message"] == "Параметр 'token' является обязательным", \
            "Валидационное сообщение не совпадает с ожидаемым"

    @allure.step("Проверка сообщения об обязательности заполнения параметра")
    def check_required_fields_error_response(self, response, fields_name):
        assert response.status_code == 400, "Статус код ответа не совпадает с ожидаемым"
        expected_message = f"Параметр '{fields_name}' является обязательным"
        AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)
