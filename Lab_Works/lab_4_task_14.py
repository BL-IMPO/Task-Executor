"""
    Task:
    1. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет
    через 3, 6, 9, ..., 24 часа, если первоначально была одна амеба. Решить задачу используя
    циклическую конструкцию for.
    2. Вывести таблицу значений функции y = -0.5x + x. Значения аргумента (x) задаются минимумом,
    максимумом и шагом. Например, если минимум задан как 1, максимум равен 3, а шаг 0.5. То надо
    вывести на экран изменение x от 1 до 3 с шагом 0.5 (1, 1.5, 2, 2.5, 3) и значения функции (y) при
    каждом значении x.
    Решить задачу используя циклическую конструкцию while.
"""


def lab_4_task_14_1():
    print("Part 1.")
    amoebas = 1

    for hour in range(3, 25, 3):
        amoebas *= 2
        print("Hour ", hour, "; Amoebas ", amoebas)


def lab_4_task_14_2():

    x_min = float(input("Введите минимум для 'x': "))
    x_max = float(input("Введите максимум для 'x': "))
    x_step = float(input("Введите шаг для 'x': "))

    while x_min <= x_max:
        print("Шаг: ", x_min, "; y: ", -0.5 * x_min + x_min)
        x_min += x_step


if __name__ == "__main__":
    lab_4_task_14_1()
    lab_4_task_14_2()