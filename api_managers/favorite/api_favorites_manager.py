import allure
import requests
from api_managers.validations.favorite.api_favorite_validator import ApiFavoriteValidator
from config import TEST_URL
class ApiFavoritesManager:
    """
    API менеджер для работы с favorite (создание избранного места)

    Предоставляет методы:
    - создание избранного места пользователя,-
    - отправка запроса на создание без токена (для тестирования ошибок авторизации).

    Использует токен авторизации для доступа к эндпоинту /favorites.
    """
    def __init__(self, token):
        self.url = TEST_URL + "/favorites"
        self.token = token
        self.validator = ApiFavoriteValidator()

    @allure.step("Создание избранного места пользователя")
    def create_favorite(self, data, token = None):
        token_source = self.token
        if token is not None:
            token_source = token
        response = requests.post(self.url, data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded',
                                          'Cookie': f"token={token_source}"})
        return response
    @allure.step("Отправка запроса на создание избранного места без токена")
    def send_create_favorite_without_token(self, data):
        response = requests.post(self.url, data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return response