"""
Выполнил Прокофьев А.А.
Фт-210008
"""

from utils import get_coord, check_color, get_figure
from chess import ChessTable, ChessFigure
import behaviors
from logger import logger, LogLevel


def main():
    """
    Функция с запуском
    """
    # ввод координат
    logger.log(LogLevel.INFO.value, "Ввод координат")
    first_x = get_coord("Введите целое число k в пределах [1; 8]")
    first_y = get_coord("Введите целое число l в пределах [1; 8]")
    second_x = get_coord("Введите целое число m в пределах [1; 8]")
    second_y = get_coord("Введите целое число n в пределах [1; 8]")
    logger.log(LogLevel.INFO.value, "Ввод координат без ошибок")

    # ввод типа фигуры
    chess_figure = get_figure()
    logger.log(LogLevel.INFO.value, "Ввод типа фигуры без ошибок")

    logger.log(LogLevel.INFO.value, "Выполнение задания а")
    response = "одного" if check_color(first_x, first_y, second_x, second_y) else "разного"
    print("а) Поля", response ,"цвета") # задание а
    logger.log(LogLevel.INFO.value, "Задание выполнено без ошибок")

    if chess_figure == ChessFigure.BISHOP: # слон
        behaviors.bishop(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.CASTLE: # ладья
        behaviors.castle(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        behaviors.knight(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        behaviors.queen(first_x, first_y, second_x, second_y)
    logger.log(LogLevel.INFO.value, "Задания б и в закончены без ошибок")

    # задание со звёздочкой
    logger.log(LogLevel.INFO.value, "Выполнение задания со звёздочкой")
    print()
    print("Вывод шахматной доски:")
    print()

    chess_table = ChessTable()
    chess_table.match_point(first_x, first_y) # точки k, l
    chess_table.match_point(second_x, second_y) # точки m, n
    chess_table.print()
    logger.log(LogLevel.INFO.value, "Задание со звёздочкой выполнено")


# запуск программы
if __name__ == "__main__":
    logger.log(LogLevel.INFO.value, "Программа запущена через команду `py app.py`")
    main()
