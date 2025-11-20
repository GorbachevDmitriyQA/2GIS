import allure
import pytest

from api_managers.api_auth_manager import ApiAuthManager
from api_managers.api_favorites_manager import ApiFavoritesManager


@allure.title("Проверка успешного создания избранного места с валидными данными")
@pytest.mark.parametrize('favorite_data', ['success_favorite_create.json',
'success_favorite_create2.json','success_favorite_create3.json'], indirect=True)
def test_success_favorite_create(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_success_favorite_create_response(response, favorite_data)

@allure.title("Проверка обязательной передачи токена авторизации в запросе на создание избранного места")
@pytest.mark.parametrize('favorite_data', ['success_favorite_create.json'], indirect=True)
def test_check_unauthorized(favorite_data):
    favorite_manager = ApiFavoritesManager(None)
    response = favorite_manager.send_create_favorite_without_token(data=favorite_data)
    favorite_manager.validator.check_unauthorized_error_response(response)

@allure.title("Проверка обязательности заполнения параметра title")
@pytest.mark.parametrize('favorite_data', ['title_required.json'], indirect=True)
def test_required_title_fields(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_required_fields_error_response(response, fields_name="title")

@allure.title("Проверка обязательности заполнения параметра lat")
@pytest.mark.parametrize('favorite_data', ['lat_required.json'], indirect=True)
def test_required_latitude_fields(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_required_fields_error_response(response, fields_name="lat")

@allure.title("Проверка обязательности заполнения параметра lon")
@pytest.mark.parametrize('favorite_data', ['lon_required.json'], indirect=True)
def test_required_longitude_fields(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_required_fields_error_response(response, fields_name="lon")

@allure.title("Проверка передачи валидных значений параметра color")
@pytest.mark.parametrize('favorite_data', ['success_color_param.json'], indirect=True)
def test_color_param_value(favorite_data):
    api_auth_manager = ApiAuthManager()
    favorite_manager = ApiFavoritesManager(None)
    color_value_list = ["BLUE", "GREEN", "RED", "YELLOW"]
    for color in color_value_list:
        favorite_data["color"] = color
        token = api_auth_manager.get_token()
        response = favorite_manager.create_favorite(data=favorite_data, token = token)
        favorite_manager.validator.check_success_favorite_create_response(response, favorite_data)
