import allure
import pytest
from api_managers.auth.api_auth_manager import ApiAuthManager
from api_managers.favorite.api_favorites_manager import ApiFavoritesManager
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

@allure.title("Проверка валидации при передаче невалидного токена авторизации при создании избранного места")
@pytest.mark.parametrize('favorite_data', ['success_favorite_create.json'], indirect=True)
def test_check_invalid_token(favorite_data):
    favorite_manager = ApiFavoritesManager(None)
    token = "2abac1c20fbf44778c1b8e55caae62dd"
    response = favorite_manager.create_favorite(data=favorite_data, token=token)
    favorite_manager.validator.check_incorrect_auth_token(response)

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
