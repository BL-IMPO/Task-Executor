def triangle_square(a):
    return (a**2 * 3**(1/2))/4


def lab_7_task_1():
    a = float(input("Введите сторону а правильного шестиугольника: "))
    print("Площадь шестиугольника: ",  3 * triangle_square(a) * 2)


def rectangle_square(a, b):
    return a * b


def lab_7_task_2():

    for i in range(3):
        a, b = map(float, input(f"Введите a и b прямоугольника {i+1}: ").split())
        print(f"Площадь прямоугольника {i+1}: {rectangle_square(a, b)}")


if __name__ == "__main__":
    lab_7_task_1()
    lab_7_task_2()
