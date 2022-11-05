"""
Классы связанные с шахматами
"""

from enum import Enum

COORD_MIN = 0
COORD_MAX = 8

class ChessFigure(Enum):
    """
    Типы доступных фигур
    """

    BISHOP = "слон"
    CASTLE = "ладья"
    KNIGHT = "конь"
    QUEEN = "ферзь"


class ChessTable:
    """
    Шахматная доска
    """

    def __init__(self) -> None:
        self._matched_fields = []


    def match_point(self, point_x: int, point_y: int) -> None:
        """
        Отметить точку на доске
        """

        if not self.check_point(point_x, point_y):
            self._matched_fields.append((point_x, point_y))


    def check_point(self, point_x: int, point_y: int) -> bool:
        """
        Проверить, отмечена ли точка на доске
        """

        return (point_x, point_y) in self._matched_fields


    def print(self) -> None:
        """
        Вывести доску в формате ascii таблицы
        """

        # вывод первой линии
        print("+", end="")

        for j in range(COORD_MAX):
            print("---", end="")
            print("+", end="")

        print()

        # вывод построчно всех полей
        for i in range(COORD_MAX):
            print("|", end="")
            for j in range(COORD_MAX):
                # отмечено ли поле
                field = "*" if self.check_point(i, COORD_MAX - j) else "_"
                print(f" {field} |", end="")

            print() # перенос строки

            print("+", end="")

            for j in range(COORD_MAX):
                print("---+", end="")

            print()
