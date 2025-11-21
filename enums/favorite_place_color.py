from enum import Enum
class FavoritePlaceColor(Enum):
     """
     Перечисление доступных значений для параметра color
     Используется в:
     - эндпоинт /favorite (создание избранного места пользователя)
     """
     BLUE = 'BLUE'
     RED = 'RED',
     GREEN = "GREEN",
     YELLOW = "YELLOW"