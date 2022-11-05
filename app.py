"""
Главный скрипт
"""

from utils import get_pos, check_pos, wrap_input, check_danger
from chess_table import ChessTable, ChessFigure


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

    print("б) ", end="") # задание б
    if chess_figure == ChessFigure.BISHOP: # слон
        check_danger(check_pos(first_x, first_y, second_x, second_y))

    elif chess_figure == ChessFigure.CASTLE: # ладья
        check_danger(first_x == second_x or first_y == second_y)

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        check_danger(abs(first_x - second_x) * abs(first_y - second_y) == 2)

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        check_danger(first_x == second_x or first_y == second_y or \
            abs(first_x-second_x) == abs(first_y = second_y))

    print("в) ", end="") # задание в
    if chess_figure == ChessFigure.BISHOP: # слон
        if not check_pos(first_x, first_y, second_x, second_y):
            print("Невозможно, т.к. различаются цвета полей")

        elif abs(first_x - second_x) == abs(first_x - second_y):
            print("Можно!")

        else:
            pass # закончить

    elif chess_figure == ChessFigure.CASTLE: # ладья
        if first_x == second_x or first_y == second_y:
            print("Можно!")

        else:
            print("Первый ход: {k}:{l}-{m}:{l}; Второй ход {m}:{l}-{m}:{n}".format(
                k=first_x+1, l=first_y+1,
                m=second_x+1, n=second_y+1))

    elif chess_figure == ChessFigure.KNIGHT: # Конь
        if abs(first_x - second_x) * abs(first_y - second_y) == 2:
            print("Можно!")

        else:
            pass # закончить

    elif chess_figure == ChessFigure.QUEEN: # ферзь
        if first_x == second_x or first_y == second_y or \
            abs(first_x-second_x) == abs(first_y = second_y):
            print("Можно!")

        else:
            print("Первый ход: {k}:{l}-{m}:{l}; Второй ход {m}:{l}-{m}:{n}".format(
                k=first_x+1, l=first_y+1,
                m=second_x+1, n=second_y+1))

    # задание со звёздочкой
    chess_table = ChessTable()
    chess_table.match_point(first_x, first_y) # точки k, l
    chess_table.match_point(second_x, second_y) # точки m, n
    chess_table.print()


# запуск программы
if __name__ == "__main__":
    main()
