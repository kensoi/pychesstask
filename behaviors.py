"""
Выполнил Прокофьев А.А.
Фт-210008
"""

from utils import check_danger, check_color, check_coord, knight_danger, bishop_danger
from chess import KNIGHTS_MOVES, BISHOP_MOVES
from logger import logger, LogLevel


def bishop(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица слона
    """

    # задание б
    logger.log(LogLevel.INFO.value, "Выполнение задания б")
    check_danger(check_color(first_x, first_y, second_x, second_y))
    logger.log(LogLevel.INFO.value, "Задание б выполнено")

    # задание в
    logger.log(LogLevel.INFO.value, "Выполнение задания в")
    if not check_color(first_x, first_y, second_x, second_y):
        print("в) Невозможно, т.к. различаются цвета полей")

    elif bishop_danger(first_x, first_y, second_x, second_y):
        print("в) Можно в один ход")
        logger.log(LogLevel.INFO.value, "Задание в выполнено в один ход")

    else:
        copied_x = first_x
        copied_y = first_y

        for move_variation in BISHOP_MOVES:
            distance = 0
            distance_loop = False

            while True:
                first_x = copied_x + move_variation[0] * distance
                first_y = copied_y + move_variation[1] * distance

                # if first_x > COORD_MAX or first_x < COORD_MIN:
                if not check_coord(first_x):
                    break

                if not check_coord(first_y):
                    break

                if bishop_danger(first_x, first_y, second_x, second_y):
                    distance_loop = True
                    print("в) Можно в 2 хода: ")
                    print(("[1] {init_x}:{init_y}-{sec_x}:{sec_y}\n" + \
                        "[2] {sec_x}:{sec_y}-{fin_x}:{fin_y}").format(
                        init_x = copied_x, init_y = copied_y,       # Начальные координаты
                        sec_x = first_x, sec_y = first_y,     # Координаты после хода коня
                        fin_x = second_x, fin_y = second_y))        # Конечные координаты
                    logger.log(LogLevel.INFO.value, "Задание в выполнено в два хода")
                    break

                distance += 1

            if distance_loop:
                break



def castle(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица ладьи
    """

    # задание б
    logger.log(LogLevel.INFO.value, "Выполнение задания б")
    check_danger(first_x == second_x or first_y == second_y)
    logger.log(LogLevel.INFO.value, "Задание б выполнено")

    # задание в
    logger.log(LogLevel.INFO.value, "Выполнение задания в")
    if first_x == second_x or first_y == second_y:
        print("в) Можно в один ход")
        logger.log(LogLevel.INFO.value, "Задание в выполнено в один ход")

    else:
        print("в) Можно в 2 хода: ")
        print("[1] {k}:{l}-{m}:{l}\n[2] {m}:{l}-{m}:{n}".format(
            k=first_x, l=first_y,
            m=second_x, n=second_y))
        logger.log(LogLevel.INFO.value, "Задание в выполнено в два хода")


def knight(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица коня
    """

    # задание б
    logger.log(LogLevel.INFO.value, "Выполнение задания б")
    check_danger(abs(first_x - second_x) * abs(first_y - second_y) == 2)
    logger.log(LogLevel.INFO.value, "Задание б выполнено")

    # задание в
    logger.log(LogLevel.INFO.value, "Выполнение задания в")
    if knight_danger(first_x, first_y, second_x, second_y):
        print("в) Можно в один ход")
        logger.log(LogLevel.INFO.value, "Задание в выполнено в один ход")

    else:
        # сохраняем значения, чтобы при каждом цикле был одни и те же first_x и first_y
        copied_x = first_x
        copied_y = first_y

        for move_variation in KNIGHTS_MOVES:
            first_x += move_variation[0]
            first_y += move_variation[1]

            if knight_danger(first_x, first_y, second_x, second_y):
                print("в) Можно в 2 хода: ")
                print(("[1] {init_x}:{init_y}-{sec_x}:{sec_y}\n" + \
                    "[2] {sec_x}:{sec_y}-{fin_x}:{fin_y}").format(
                    init_x = copied_x, init_y = copied_y,       # Начальные координаты
                    sec_x = first_x, sec_y = first_y,     # Координаты после хода коня
                    fin_x = second_x, fin_y = second_y))        # Конечные координаты
                logger.log(LogLevel.INFO.value, "Задание в выполнено в два хода")
                break

            first_x = copied_x
            first_y = copied_y

        else:
            print("в) Невозможно")


def queen(first_x: int, first_y: int, second_x: int, second_y: int) -> None:
    """
    Проверка заданий от лица ферзя
    """

    # задание б
    logger.log(LogLevel.INFO.value, "Выполнение задания б")
    check_danger(first_x == second_x or first_y == second_y or \
            abs(first_x - second_x) == abs(first_y - second_y))
    logger.log(LogLevel.INFO.value, "Задание б выполнено")

    # задание в
    logger.log(LogLevel.INFO.value, "Выполнение задания в")
    if first_x == second_x or first_y == second_y or \
        abs(first_x - second_x) == abs(first_y - second_y):
        print("в) Можно в один ход")
        logger.log(LogLevel.INFO.value, "Задание в выполнено в один ход")

    else:
        print("в) Можно в 2 хода: ")
        print("[1] {k}:{l}-{m}:{l}\n[2] {m}:{l}-{m}:{n}".format(
            k=first_x, l=first_y,
            m=second_x, n=second_y))
        logger.log(LogLevel.INFO.value, "Задание в выполнено в два хода")
