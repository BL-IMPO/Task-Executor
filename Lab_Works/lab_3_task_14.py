def half_perimetr(a: float, b: float, c: float) -> float:
    return (a + b + c)/2

def square(a: float, b: float, c: float) -> float:
    p = half_perimetr(a, b, c)
    return p * (p - a) * (p - b) * (p - c)

def lab_3_task_13():
    a, b, c = map(float, input("Введите стороны треугольника a, b, c: ").split(" "))

    if not a == 0 and not b == 0 and not c == 0:
        if a + b > c:
            print("Треугольник существует! Площадь равна: {0:.2f}".format(square(a, b, c)))
        elif a + c > b:
            print("Треугольник существует! Площадь равна: {0:.2f}".format(square(a, b, c)))
        elif b + c > a:
            print("Треугольник существует! Площадь равна: {0:.2f}".format(square(a, b, c)))
        else:
            print("Треугольник не существует!")
    else:
        print("Треугольник не существует!")


if __name__ == "__main__":
    lab_3_task_13()