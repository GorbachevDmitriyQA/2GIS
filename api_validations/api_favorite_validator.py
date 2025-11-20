from contextlib import nullcontext
from datetime import datetime
import allure
class ApiFavoriteValidator:
    def __init__(self):
        self.error_message = "не совпадает с ожидаемым"

    @allure.step("Проверка ответа при создании избранного места")
    def check_success_favorite_create_response(self, response, expected_data):
        assert response.status_code == 200, f"Статус код ответа {self.error_message}"
        json_data = response.json()
        created_date = json_data["created_at"]
        assert isinstance(json_data["id"], int),\
            f"id в ответе {self.error_message} типом значения integer"
        assert json_data["title"] == expected_data["title"], f"title {self.error_message}"
        assert json_data["lat"] == expected_data["lat"], f"lat {self.error_message}"
        assert json_data["lon"] == expected_data["lon"], f"lon {self.error_message}"
        if expected_data.get("color") is not None:
            assert json_data["color"] == expected_data["color"], f"color {self.error_message}"
        else: assert json_data["color"] is None, f"color значение по умолчанию (null) {self.error_message}"
        self.check_created_at_value(created_date)
        return ApiFavoriteValidator

    @allure.step("Проверка формата даты в ответе от сервера")
    def check_created_at_value(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            assert False, "Дата не соответствует формату YYYY-MM-DDThh:mm:ss±hh:mm"
        return ApiFavoriteValidator