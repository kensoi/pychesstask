"""
Главный скрипт
"""

from utils import get_pos, check_pos, wrap_input
from chess import ChessTable, ChessFigure
import behaviors

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
    chess_figure = ChessFigure(wrap_input("Введите тип фигуры >> "))

    response = "одного" if check_pos(first_x, first_y, second_x, second_y) else "разного"
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
