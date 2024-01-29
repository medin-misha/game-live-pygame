import numpy as np


def get_caged_neighbors(array, x:int = 0, y:int = 0) -> dict:
    """
        функция которая возвращает все координаты клеток и соседей

        :param array: игровое поле с клетками
        :param x: ряд
        :param y: элемент
        :return: координаты 8 клеток от клетки x,y
    """

    result = {
        "cords":(
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
        )
    }
    elem_list = []
    for number, coord in enumerate(result["cords"]):

        if 0 <= coord[0] <= array.shape[0] and\
            0 <= coord[1] <= array.shape[1]:

            elem_list.append(array[coord])
        else:
            elem_list.append(None)

    result["elements"] = np.array([elem_list[:3], elem_list[3:6], elem_list[6:9]], int)

    return result





def set_to_play_square(array, x, y):
    """
        функция в которую ты вводишь координаты середины квадрата
        и она возвращяет игровое поле с квадратом на нужных координатах

        :param array: игровое поле с клетками
        :param x: ряд
        :param y: елемент
        :return: игровое поле
    """
    result = get_caged_neighbors(array, x, y)["cords"]

    for x, y in result:

        if 0 <= x <= array.shape[0] and 0 <= y <= array.shape[1]:
            array[x, y] = 1

    return array


def life_test(array, x, y):
    """
    Функция для определения состояния клетки на следующем шаге игры "Жизнь".

    Аргументы:
    - array (list): Двумерный массив, представляющий игровое поле.
    - x (int): Координата x проверяемой клетки.
    - y (int): Координата y проверяемой клетки.

    Возвращает:
    - bool: True, если клетка будет живой на следующем шаге, иначе False.
    """
    rows = len(array)
    cols = len(array[0]) if rows > 0 else 0

    # Проверка корректности координат клетки
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return "Некорректные координаты"

    live_neighbors = 0
    current_state = array[x][y]

    # Подсчёт живых соседей для клетки
    for i in range(max(0, x - 1), min(x + 2, rows)):
        for j in range(max(0, y - 1), min(y + 2, cols)):
            if i != x or j != y:
                live_neighbors += array[i][j]

    # Применение правил "Жизни"
    if current_state == 1:
        if live_neighbors == 2 or live_neighbors == 3:
            return True
        else:
            return False
    else:
        if live_neighbors == 3:
            return True
        else:
            return False




def one_game_step(array):
    """
    Функция для выполнения одного шага в игре "Жизнь".

    Аргументы:
    - array (list): Игровое поле.

    Возвращает:
    - list: Новое игровое поле после выполнения одного шага.
    """
    #подсчёт елементов в матрице
    rows = len(array)
    cols = len(array[0]) if rows > 0 else 0

    # новая матрица на основе старой
    new_array = [
            [0 for _ in range(cols)]
        for _ in range(rows)]

    new_array = np.array(new_array, int)

    for x in range(rows):
        for y in range(cols):
            life_state = life_test(array, x, y)

            # Обновляем значение клетки в новом игровом поле
            new_array[x][y] = 1 if life_state else 0

    return new_array



