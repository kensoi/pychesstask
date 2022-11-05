"""
Выполнил Прокофьев А.А.
Фт-210008
"""

from utils import get_coord, check_color, get_figure
from chess import ChessTable, ChessFigure
import behaviors


def main():
    """
    Функция с запуском
    """
    # ввод координат
    first_x = get_coord("Введите целое число k в пределах [1; 8]")
    first_y = get_coord("Введите целое число l в пределах [1; 8]")
    second_x = get_coord("Введите целое число m в пределах [1; 8]")
    second_y = get_coord("Введите целое число n в пределах [1; 8]")

    # ввод типа фигуры
    chess_figure = get_figure()

    response = "одного" if check_color(first_x, first_y, second_x, second_y) else "разного"
    print("а) Поля", response ,"цвета") # задание а

    if chess_figure == ChessFigure.BISHOP: # слон
        behaviors.bishop(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.CASTLE: # ладья
        behaviors.castle(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        behaviors.knight(first_x, first_y, second_x, second_y)

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        behaviors.queen(first_x, first_y, second_x, second_y)

    # задание со звёздочкой
    print()
    print("Вывод шахматной доски:")
    print()

    chess_table = ChessTable()
    chess_table.match_point(first_x, first_y) # точки k, l
    chess_table.match_point(second_x, second_y) # точки m, n
    chess_table.print()


# запуск программы
if __name__ == "__main__":
    main()
