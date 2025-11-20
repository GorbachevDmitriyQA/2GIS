import allure
import requests
class ApiAuthManager:
    def __init__(self):
        self.url = "https://regions-test.2gis.com/v1/auth/tokens"

    @allure.step("Получение токена авторизации")
    def get_token(self):
        token = requests.post(self.url).cookies.get('token')
        return token