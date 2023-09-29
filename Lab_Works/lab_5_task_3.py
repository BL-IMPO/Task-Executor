
def lab_5_task_3():
    string = input("Введите строку: ")

    print("Строка до замены: ", string)

    ls_str = list(string.split("."))
    count_point = len(string.split(".")) - 1
    string = ''.join(ls_str)

    print("Строка после замены: ", string)
    print("Количество произведенных операций: ", count_point)


if __name__ == "__main__":
    lab_5_task_3()