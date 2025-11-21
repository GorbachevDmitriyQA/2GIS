import allure
import requests
from config import TEST_URL
class ApiAuthManager:
    """
    Класс API менеджер для работы с авторизацией

    Предоставляет метод для получения токена авторизации
    от сервиса 2GIS. Использует эндпоинт /auth/tokens.
    """
    def __init__(self):
        self.url = TEST_URL + "/auth/tokens"

    @allure.step("Получение токена авторизации")
    def get_token(self):
        token = requests.post(self.url).cookies.get('token')
        return token