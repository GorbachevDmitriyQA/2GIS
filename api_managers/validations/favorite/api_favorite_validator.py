from datetime import datetime
import allure
from enums.favorite_place_color import FavoritePlaceColor
from helper.validator_hepler import AssertionHelper
class ApiFavoriteValidator:
    """
    Менеджер по работе с проверками для эндпоинта /favorite
    (создание избранного места)
    """
    @allure.step("Проверка ответа при создании избранного места")
    def check_success_favorite_create_response(self, response, expected_data):
        AssertionHelper.check_status_code(response.status_code, 200)
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
        AssertionHelper.check_status_code(response.status_code, 401)
        assert response.json()["error"]["message"] == "Параметр 'token' является обязательным", \
            "Валидационное сообщение не совпадает с ожидаемым"

    @allure.step("Проверка сообщения об обязательности заполнения параметра")
    def check_required_fields_error_response(self, response, fields_name):
        assert response.status_code == 400, "Статус код ответа не совпадает с ожидаемым"
        expected_message = f"Параметр '{fields_name}' является обязательным"
        AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)

    @allure.step("Проверка валидационного сообщения на недопустимые значения для поля latitude")
    def check_latitude_validation(self, response, expected_data):
        AssertionHelper.check_status_code(response.status_code, 400)
        expected_message = ""
        if not isinstance(expected_data["lat"], int):
            expected_message = "Параметр 'lat' должен быть числом"
        elif expected_data["lat"] > 90:
            expected_message = "Параметр 'lat' должен быть не более 90"
        elif expected_data["lat"] < -90:
            expected_message = f"Параметр 'lat' должен быть не менее -90"
        AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)

    @allure.step("Проверка валидационного сообщения на недопустимые значения для поля longitude")
    def check_longitude_validation(self, response, expected_data):
        AssertionHelper.check_status_code(response.status_code, 400)
        expected_message = ""
        if not isinstance(expected_data["lon"], int):
            expected_message = "Параметр 'lon' должен быть числом"
        elif expected_data["lon"] > 180:
            expected_message = "Параметр 'lon' должен быть не более 180"
        elif expected_data["lon"] < -180:
            expected_message = f"Параметр 'lon' должен быть не менее -180"
        AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)

    @allure.step("Проверка валидационного сообщения на недопустимые значения для поля color")
    def check_color_validation(self, response, expected_data):
        AssertionHelper.check_status_code(response.status_code, 400)
        expected_message = "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"
        if expected_data["color"] is None:
            assert False, "Параметр color отсутствует в списке ожидаемых значений"
        elif expected_data["color"] not in FavoritePlaceColor:
            AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)

    @allure.step("Проверка валидационного сообщения при передаче некорректного токена авторизации")
    def check_incorrect_auth_token(self, response):
        AssertionHelper.check_status_code(response.status_code, 401)
        expected_message = "Передан несуществующий или «протухший» 'token'"
        AssertionHelper.are_equals(response.json()["error"]["message"], expected_message)


