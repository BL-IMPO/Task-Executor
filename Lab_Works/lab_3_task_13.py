
def square(a: float, b: float) -> float:
    return (a + b)/2


def lab_3_task_13():
    a, b, c = map(float, input("Введите стороны треугольника a, b, c: ").split(" "))

    if not a == 0 and not b == 0 and not c == 0:
        if c**2 == a**2 + b**2:
            print("Треугольник существует! Площадь равна: {0:.2f}".format(square(a, b)))
        else:
            print("Треугольник не существует!")
    else:
        print("Треугольник не существует!")


if __name__ == "__main__":
    lab_3_task_13()