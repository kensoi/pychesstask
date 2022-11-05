"""
Выполнил Прокофьев А.А.
Фт-210008
"""

from chess import COORD_MIN, COORD_MAX, ChessFigure


def wrap_input(text_to_print:str) -> str:
    """
    обёртка вокруг для красивого оформления
    """

    return input(text_to_print + " >> ").lower()


def check_coord(coord:int):
    """
    проверка координаты на соответствие пределам шахматной доски
    """

    return coord >= COORD_MIN and coord < COORD_MAX


def get_coord(text_to_print:str) -> int:
    """
    Получить значение координаты в допустимых значениях
    """

    while True:
        try:
            coord = int(wrap_input(text_to_print))

        except ValueError as value_error: # ошибка перевода в int
            print(f"Введите число! (Ошибка: {value_error}")
            continue

        if check_coord(coord): # координата выходит за пределы ОДЗ
            return coord

        print("Число выходит за пределы допустимых выражений!")


def check_color(first_x:int, first_y:int, second_x:int, second_y:int) -> bool:
    """
    Проверить одного ли цвета клетки (first_x, first_y) и (second_x, second_y)
    """

    return (first_x + first_y + second_x + second_y) % 2 == 0


def check_danger(statement: bool) -> None:
    """
    обёртка вокруг bool и print
    """

    print("б) угрожает" if statement else "б) не угрожает")


def knight_danger(first_x: int, first_y: int,
        second_x: int, second_y: int) -> bool:
    """
    Угрожает ли конь клетке (second_x, second_y) с позиции (first_x, first_y)
    """

    return abs(first_x - second_x) * abs(first_y - second_y) == 2


def bishop_danger(first_x: int, first_y: int,
        second_x: int, second_y: int) -> bool:
    """
    Угрожает ли слон клетке (second_x, second_y) с позиции (first_x, first_y)
    """

    return abs(first_x - second_x) == abs(first_y - second_y)


def get_figure() -> ChessFigure:
    """
    функция получения фигуры
    """

    while True:
        try:
            figure = wrap_input("Введите тип фигуры (слон, ферзь, конь, ладья)")

            if figure == "королева":
                figure = "ферзь"

            return ChessFigure(figure)

        except ValueError as value_error:
            print(f"Типа \"{figure}\" не существует! (Ошибка: {value_error}")
