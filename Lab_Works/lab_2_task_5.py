from math import *


def lab_2_task_5():
    x, y, z = map(float, input("Введите три числа x, y, z: ").split(" "))
    a = (2 * cos(x - pi/6))/(1/2 + sin(y)**2)
    b = 1 + (z**2)/(3 + (z**2)/5)

    print("a = ", a, "; b = ", b)


if __name__ == "__main__":
    lab_2_task_5()