import pytest
from api_managers.api_favorites_manager import ApiFavoritesManager
from api_validations.api_favorite_validator import ApiFavoriteValidator


@pytest.mark.parametrize('favorite_data', ['success_favorite_create.json',
'success_favorite_create2.json','success_favorite_create3.json'], indirect=True)
def test_success_favorite_create(favorite_data, get_token):
    favorite_manager = ApiFavoritesManager(get_token)
    response = favorite_manager.create_favorite(data=favorite_data)
    favorite_manager.validator.check_success_favorite_create_response(response, favorite_data)

@pytest.mark.parametrize('favorite_data', ['success_favorite_create.json'], indirect=True)
def test_check_unauthorized(favorite_data):
    favorite_manager = ApiFavoritesManager(None)
    response = favorite_manager.send_create_favorite_without_token(data=favorite_data)

    assert response.status_code == 401
    assert response.json()["error"]["message"] == "Параметр 'token' является обязательным",\
        "Валидационное сообщение не совпадает с ожидаемым"
