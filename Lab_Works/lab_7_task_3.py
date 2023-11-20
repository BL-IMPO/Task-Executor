def hypotenuse(a, b):
    return (a**2 + b**2) ** (1/2)


def lab_7_task_3_1():
    a1, b1 = map(float, input("Введите катеты первого пр. треугольника: ").split())
    a2, b2 = map(float, input("Введите катеты второго пр. треугольника: ").split())

    if hypotenuse(a1, b1) > hypotenuse(a2, b2):
        print("Первая гипотенуза больше, она равна: ", hypotenuse(a1, b1))
        print("Вторая гипотенуза меньше, она равна: ", hypotenuse(a2, b2))
    else:
        print("Вторая гипотенуза больше, она равна: ", hypotenuse(a2, b2))
        print("Первая гипотенуза меньше, она равна: ", hypotenuse(a1, b1))


def sort_word(word):
    return ''.join(sorted(word))


def lab_7_task_3_2():
    s = input("Введите строку: ").split()
    new_s = ''

    for i in s:
        new_s += " " + sort_word(i)

    print("Строка с отсортированными словами: ", new_s)


if __name__ == "__main__":
    lab_7_task_3_1()
    lab_7_task_3_2()