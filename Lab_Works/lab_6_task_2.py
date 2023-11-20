
def lab_6_task_2_1():
    arr = list(map(int, input("Введите массив через пробел: ").split(" ")))
    min_num = arr[0]
    min_index = 0

    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_index = i

    print("Индекс минимального элемента: ", min_index, "; Минимальный элемент: ", min_num)

    # Short way.
    # print("Индекс минимального элемента: ", arr.index(min(arr)), "; Минимальный элемент: ", min(arr))


def lab_6_task_2_2():
    from random import randint

    arr = [randint(-100, 100) for _ in range(20)]
    pos_arr = []
    neg_arr = []

    for i in arr:
        if i >= 0:
            pos_arr.append(i)
        else:
            neg_arr.append(i)

    print("Исходный массив: ", arr)
    print("Массив положительных элементов: ", pos_arr)
    print("Массив отрицательных элементов: ", neg_arr)


if __name__ == "__main__":
    lab_6_task_2_1()
    lab_6_task_2_2()
