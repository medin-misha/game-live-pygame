import numpy as np
import random
from utils.game_rules import set_to_play_square


class GameLife:
    def __init__(self, field_size:tuple = (50, 50)):
        self.field_size = field_size
        self.playing_field = np.array(
            [
                [0 for _ in range(self.field_size[1])]
                for _ in range(self.field_size[0])
            ]
        )

    def life_test(self, x:int, y:int):
        """
        Функция для определения состояния клетки на следующем шаге игры "Жизнь".

        Аргументы:
        - array (list): Двумерный массив, представляющий игровое поле.
        - x (int): Координата x проверяемой клетки.
        - y (int): Координата y проверяемой клетки.

        Возвращает:
        - bool: True, если клетка будет живой на следующем шаге, иначе False.
        """


            # # Проверка корректности координат клетки
            # if x < 0 or y < 0 or x >= self.field_size[0] or y >= self.field_size[1]:
            #     return "Некорректные координаты"

        live_neighbors = 0
        current_state = self.playing_field[x][y]

        # Подсчёт живых соседей для клетки
        for i in range(max(0, x - 1), min(x + 2, self.field_size[0])):
            for j in range(max(0, y - 1), min(y + 2, self.field_size[1])):
                if i != x or j != y:
                    live_neighbors += self.playing_field[i][j]

        # Применение правил "Жизни"
        if current_state == 1 and live_neighbors == 2 or live_neighbors == 3 or live_neighbors == 3:
            return 1
        else:
            return 0

    def step(self):
        """
        Функция для выполнения одного шага в игре "Жизнь".

        Аргументы:
        - array (list): Игровое поле.

        Возвращает:
        - list: Новое игровое поле после выполнения одного шага.
        """
        # подсчёт елементов в матрице


        # новая матрица на основе старой
        new_array = self.playing_field.copy()
        new_array.fill(0)



        for x in range(self.field_size[0]):
            for y in range(self.field_size[1]):
                life_state = self.life_test(x = x, y = y)

                # Обновляем значение клетки в новом игровом поле
                new_array[x][y] = life_state

        self.playing_field = new_array
    def create_figure(self, cords: tuple = (0, 0), figure:str = "random"):
        """
        Создание квадрата на указанных координатах
        :param cords: координаты cords[0] - x cords[1] - y, по умолчанию 0, 0
        :return:
        """
        match figure:
            case "square":
                self.playing_field = set_to_play_square(
                    self.playing_field,
                    x=cords[0], y=cords[1]
                )
            case "random":
                for x in range(self.playing_field.shape[0]):
                    for y in range(self.playing_field.shape[1]):
                        self.playing_field[x][y] = random.randint(0,1)
            case "random_call":
                x = random.randint(0, self.field_size[0]-1)
                y = random.randint(0, self.field_size[1]-1)
                self.playing_field[x][y] = 1
    def show(self):
        return self.playing_field