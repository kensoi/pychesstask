"""
Скрипт с поведениями фигур
"""
from utils import check_danger, check_pos

def bishop(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица слона
    """

    # задание б
    check_danger(check_pos(first_x, first_y, second_x, second_y))

    # задание в
    if not check_pos(first_x, first_y, second_x, second_y):
        print("в) Невозможно, т.к. различаются цвета полей")

    elif abs(first_x - second_x) == abs(first_x - second_y):
        print("в) Можно в один ход")

    else:
        pass # закончить

def castle(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица ладьи
    """

    # задание б
    check_danger(first_x == second_x or first_y == second_y)

    # задание в
    if first_x == second_x or first_y == second_y:
        print("в) Можно в один ход")

    else:
        print("в) Можно в 2 хода: ")
        print("[1] {k}:{l}-{m}:{l}\n[2] {m}:{l}-{m}:{n}".format(
            k=first_x+1, l=first_y+1,
            m=second_x+1, n=second_y+1))



def knight(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица коня
    """

    # задание б
    check_danger(abs(first_x - second_x) * abs(first_y - second_y) == 2)

    # задание в
    if abs(first_x - second_x) * abs(first_y - second_y) == 2:
        print("в) Можно в один ход")

    else:
        pass # закончить


def queen(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица ферзя
    """

    # задание б
    check_danger(first_x == second_x or first_y == second_y or \
            abs(first_x-second_x) == abs(first_y = second_y))

    # задание в
    if first_x == second_x or first_y == second_y or \
        abs(first_x-second_x) == abs(first_y = second_y):
        print("в) Можно в один ход")

    else:
        print("в) Можно в 2 хода: ")
        print("[1] {k}:{l}-{m}:{l}\n[2] {m}:{l}-{m}:{n}".format(
            k=first_x+1, l=first_y+1,
            m=second_x+1, n=second_y+1))
