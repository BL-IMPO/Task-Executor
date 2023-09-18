from math import *


def lab_2_task_6():
    x, y, z = map(float, input("Введите три числа x, y, z: ").split(" "))
    a = (1 + sin(x + y)**2)/(2 + abs(x - (2 * x)/(1 + x**2 * y**2))) + x
    b = cos(atan(1/z))**2

    print("a = ", a, "; b = ", b)


if __name__ == "__main__":
    lab_2_task_6()