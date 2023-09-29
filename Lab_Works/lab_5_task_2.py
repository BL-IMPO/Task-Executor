
def lab_5_task_2():

    s1 = input("Введите строку: ")

    print("Строка до замены: ", s1)

    symb_count = s1.count(":")
    s1 = s1.replace(":", "%")

    print("Строка после замены: ", s1)
    print("Количество произведенных замен: ", symb_count)


if __name__ == "__main__":
    lab_5_task_2()