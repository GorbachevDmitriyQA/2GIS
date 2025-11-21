import allure
import pytest
from api_managers.favorite.api_favorites_manager import ApiFavoritesManager

@allure.title("Проверка передачи невалидных значений широты")
@pytest.mark.parametrize('favorite_data', ['latitude_value_tests1.json',
'latitude_value_tests2.json', 'latitude_value_tests3.json'], indirect=True)
def test_latitude_incorrect_value(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_latitude_validation(response, favorite_data)

@allure.title("Проверка передачи невалидных значений долготы")
@pytest.mark.parametrize('favorite_data', ['longitude_value_tests1.json',
'longitude_value_tests2.json', 'longitude_value_tests3.json'],indirect=True)
def test_longitude_incorrect_value(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_longitude_validation(response, favorite_data)


@allure.title("Проверка передачи невалидных значений цвета")
@pytest.mark.parametrize('favorite_data', ['color_value_tests1.json',
'color_value_tests2.json', 'color_value_tests3.json'],indirect=True)
def test_color_incorrect_value(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_color_validation(response, favorite_data)
