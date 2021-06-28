my_dict = {
    'name': [],
    'age': [],
    'sex': []
}

while True:

    print("Заполни данные как можно больше людей, нажми 0 если захочешь выйти")
    name = input("Введи свое имя: ")
    if name == '0':
        break
    age = input("Введи свой возраст: ")
    sex = input("Введи свой пол: ")

    d1 = dict(name=name,age=age,sex=sex)

    my_dict.update(d1)

print(my_dict)




