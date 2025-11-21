import allure
import pytest
from api_managers.favorite.api_favorites_manager import ApiFavoritesManager


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