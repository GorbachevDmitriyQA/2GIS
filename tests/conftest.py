import json
import os
from pathlib import Path
import allure
import pytest
from api_managers.api_auth_manager import ApiAuthManager


@pytest.fixture(scope="function")
@allure.step("Получение токена авторизации")
def get_token():
    api_manager = ApiAuthManager()
    token = api_manager.get_token()
    return token


@pytest.fixture(scope='function')
@allure.step("Получение тест даты")
def favorite_data(request):
    this_dir = Path(__file__).parent
    testdata_dir = (this_dir.parent / 'test_data').resolve()
    final_path = os.path.join(testdata_dir, request.param)
    with open(final_path, 'r', encoding='utf-8') as f:
        data = f.read()
    payload = json.loads(data)
    return payload