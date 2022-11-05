"""
Выполнил Прокофьев А.А.
Фт-210008
"""

from enum import Enum
from logger import logger, LogLevel


COORD_MIN, COORD_MAX = 1, 9 # Пределы значений; в математическом виде: [1; 8]
FIELD_NAME_HORIZONTAL = "ABCDEFGH"
FIELD_NAME_VERTICAL = list(range(COORD_MIN+1, COORD_MAX+1))
KNIGHTS_MOVES = [(1, 2), (2, 1), (-1, 2), (2, -1),
    (1, -2), (-2, 1), (-1, -2), (-2, -1)]
BISHOP_MOVES = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


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

        logger.log(LogLevel.INFO.value, "Установка точки на доску")

        if self.check_point(point_x, point_y):
            logger.log(LogLevel.WARNING, "Точка уже существует")

        else:
            self._matched_fields.append((point_x, point_y))
            logger.log(LogLevel.INFO.value, "Точка установлена")


    def check_point(self, point_x: int, point_y: int) -> bool:
        """
        Проверить, отмечена ли точка на доске
        """

        logger.log(LogLevel.INFO.value, "Проверка наличия точки на доске")
        return (point_x, point_y) in self._matched_fields


    def print(self) -> None:
        """
        Вывести доску в формате ascii таблицы
        """

        logger.log(LogLevel.INFO.value, "Начало вывода доски")

        # вывод первой линии
        print("", "+", sep = "\t", end = "")

        logger.log(LogLevel.INFO.value, "Вывод начальной линии")
        for j in range(COORD_MIN, COORD_MAX):
            logger.log(LogLevel.INFO.value, "Вывод колонки")
            print("---", end = "")
            print("+", end = "")

        print()
        logger.log(LogLevel.INFO.value, "Начальная линия закончилась, переходим к циклу")

        # вывод построчно всех полей
        for i in range(COORD_MAX - 1, COORD_MIN - 1, -1): # по вертикали -> y
            logger.log(LogLevel.INFO.value, "Вывод линии")
            print(i, "|", sep = "\t", end = "")

            for j in range(COORD_MIN, COORD_MAX): # по горизонтали -> x
                # отмечено ли поле
                logger.log(LogLevel.INFO.value, "Вывод колонки")
                field = "*" if self.check_point(j, i) else " "
                print(f" {field} |", end = "")

            print() # перенос строки
            logger.log(LogLevel.INFO.value, "Вывод переносной линии")

            print("", "+", sep = "\t", end = "")

            for j in range(COORD_MIN, COORD_MAX):
                print("---+", end="")

            print()
            logger.log(LogLevel.INFO.value, "Вывод линии закончен")
        logger.log(LogLevel.INFO.value, "Доска выведена")
        print()
        print()
        print("",
            " " + "".join(list(map(lambda x: " " + x + "  ", FIELD_NAME_HORIZONTAL))),
            sep = "\t")
        logger.log(LogLevel.INFO.value, "Буквы по горизонтали выведены")


if __name__ == "__main__":
    test = ChessTable()
    test.match_point(3, 4)
    test.match_point(5, 6)
    test.print()
