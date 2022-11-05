"""
рабочие инструменты
"""

from chess import COORD_MIN, COORD_MAX

def wrap_input(text_to_print:str) -> str:
    """
    обёртка вокруг для красивого оформления
    """

    return input(text_to_print + " >> ").lower()


def get_pos(text_to_print:str) -> int:
    """
    Получить значение координаты в допустимых значениях
    """

    while True:
        try:
            coord = int(wrap_input(text_to_print))

        except ValueError as value_error: # ошибка перевода в int
            print(f"Введите число! (Ошибка: {value_error}")
            continue

        if coord < COORD_MIN or coord > COORD_MAX: # координата выходит за пределы ОДЗ
            print("Число выходит за пределы допустимых выражений!")
            continue

        return coord


def check_pos(first_x:int, first_y:int, second_x:int, second_y:int) -> bool:
    """
    Проверить одного ли цвета клетки (first_x, first_y) и (second_x, second_y)
    """

    return (first_x + first_y + second_x + second_y) % 2 == 0


def check_danger(statement: bool) -> None:
    """
    обёртка вокруг bool и print
    """

    print("угрожает" if statement else "не угрожает")
