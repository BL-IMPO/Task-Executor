from random import randint


def lab_6_task_3_1():
    n = randint(5, 15)
    D = [randint(1, 50) for _ in range(n)]

    summ = 0
    for i in range(1, n, 2):
        summ += D[i]

    print("Массив D: ", D)
    print("Сумма: ", summ)


def lab_6_task_3_2():
    arr = [randint(1, 25) for _ in range(8)]
    print("Исходный массив: ", arr)

    for i in range(len(arr)):
        if arr[i] < 15:
            arr[i] *= arr[i]

    print("Преобразованый массив: ", arr)


if __name__ == "__main__":
    lab_6_task_3_1()
    lab_6_task_3_2()