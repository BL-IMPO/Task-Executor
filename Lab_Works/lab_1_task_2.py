"""
Имя, , Дата рождения, Образование
- имя (;Ваше, имя?;)
- дата рождения (;Ваша дата рождения?;)
- образование (;Где Вы учитесь?;)
После этого выводила бы три строки:
"Ваше имя"
"Дата рождения"
"Вы учитесь в "
"""


def lab_1_task_2():
    name = input("Ваше, имя? ")
    date = input("Ваша дата рождения?")
    education = input("Где Вы учитесь? ")
    print("Ваше имя: {} \nДата рождения: {} \nВы учитесь в: {}".format(name, date, education))


if __name__ == "__main__":
    lab_1_task_2()