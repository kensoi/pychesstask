"""
Главный скрипт
"""

from utils import get_pos, check_pos, get_input
from chess_table import ChessTable, ChessFigure

def check_danger(statement: bool) -> None:
    """
    обёртка вокруг bool и print
    """

    print("угрожает" if statement else "не угрожает")


def main():
    """
    Функция с запуском
    """
    # ввод координат
    first_x = get_pos("Введите k")
    first_y = get_pos("Введите l")
    second_x = get_pos("Введите m")
    second_y = get_pos("Введите n")

    # ввод типа фигуры
    chess_figure = ChessFigure(get_input("Введите тип фигуры >> "))

    # задание а
    # Выяснить, являются ли поля (k, I) и (m, n) полями одного цвета.
    response = "одного" if check_pos(first_x, first_y, second_x, second_y) else "разного"
    print("а) Поля", response ,"цвета")

    # задание б
    # На поле (к, I) расположен ферзь, ладья, слон или конь (должен ввести пользователь).
    # Угрожает ли он полю (m, n)?

    print("б) ", end="")
    if chess_figure == ChessFigure.BISHOP: # слон
        check_danger(check_pos(first_x, first_y, second_x, second_y))

    elif chess_figure == ChessFigure.CASTLE: # ладья
        check_danger(first_x == second_x or first_y == second_y)

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        check_danger(abs(first_x - second_x) * abs(first_y - second_y) == 2)

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        check_danger(first_x == second_x or first_y == second_y or \
            abs(first_x-second_x) == abs(first_y = second_y))

    # задание в
    # Выяснить, можно ли с поля (k, I) одним ходом ладьи, ферзя или слона (должен ввести
    # пользователь) попасть на поле (m, n). Если нет, то выяснить, как это можно сделать за два
    # хода (указать поле, на которое приводит первый ход).

    print("в) ", end="")
    if chess_figure == ChessFigure.BISHOP: # слон
        if not check_pos(first_x, first_y, second_x, second_y):
            print("Невозможно, т.к. различаются цвета полей")

        elif abs(first_x - second_x) == abs(first_x - second_y):
            print("Можно!")

        else:
            pass

    elif chess_figure == ChessFigure.CASTLE: # ладья
        if first_x == second_x or first_y == second_y:
            print("Можно!")

        else:
            pass

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        if abs(first_x - second_x) * abs(first_y - second_y) == 2:
            print("Можно!")

        else:
            pass

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        if first_x == second_x or first_y == second_y or \
            abs(first_x-second_x) == abs(first_y = second_y):
            print("Можно!")

        else:
            pass

    # задание со звёздочкой
    chess_table = ChessTable()
    chess_table.match_point(first_x, first_y) # точки k, l
    chess_table.match_point(second_x, second_y) # точки m, n
    chess_table.print()


# запуск программы
if __name__ == "__main__":
    main()
