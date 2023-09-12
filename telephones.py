import os
file_path = os.path.realpath(__file__)
script_dir = os.path.dirname(file_path)


from pathlib import Path
path = Path(script_dir, 'data.txt')


def readall(nm):
    print("Вся телефонная книга: ")
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())


def write_1(nm):
    print('Добавляем новую запись:')
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2 + ', ' + str_new3 + ', ' + str_new4
    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)


def find_item(nm):
    item = input('Поиск по Характеристике: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())


def find_item_2(nm):
    print("Поиск записи:")
    item = input('Значение характеристики: ')
    item_type = int(
        input('Введите номер характеристики (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)


def sort_data(nm):
    list_1 = []
    item_type = int(input(
        'Введите номер характеристики для сортировки книги (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if -1<item_type<5:
        with open(nm, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                line = line.rstrip('\n')
                line = line.split(', ')
                list_1.append(line)
            list_1.sort(key=lambda person: person[item_type])
        with open(nm, 'w', encoding='utf8') as txt_file:
            for line in list_1[0:-1]:
                line = ', '.join(line)
                line = line + '\n'
                txt_file.write(line)
            line = list_1[-1]
            line = ', '.join(line)
            txt_file.write(line)

def change_item(nm):
    list_1 = []
    item_type = int(input(
        'Введите номер характеристики для поиска записи (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if -1<item_type<5:
        item_value = input('Введите значение характеристики для поиска записи: ')
        print('Введите измененные значения новой записи:')
        str_new1 = input('Фамилия: ')
        str_new2 = input('Имя: ')
        str_new3 = input('Отчество: ')
        str_new4 = input('Телефон: ')
        str_new = str_new1 + ', ' + str_new2 + ', ' + str_new3 + ', ' + str_new4 + '\n'
        with open(nm, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                line = line.split(', ')
                list_1.append(line)
        with open(nm, 'w', encoding='utf8') as txt_file:
            for line in list_1:
                if str(line[item_type]).lower() != item_value.lower():
                    line = ', '.join(line)
                    txt_file.write(line)
                else:
                    txt_file.write(str_new)


def delete_item(nm):
    list_1 = []
    item_type = int(input('Введите номер характеристики для удаления записи (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    if -1<item_type<5:
        item_value = input('Введите значение характеристики для поиска записи: ')
      
        with open(nm, 'r', encoding='utf8') as txt_file:
            for line in txt_file:
                line = line.split(', ')
                if line[item_type].lower() == item_value.lower():
                    print(*line)
                    appr = input("Удалить эту запись? (Д/Н): ")
                    if appr.lower() == 'д':
                        with open(nm, 'r', encoding='utf8') as txt_file:
                            for line in txt_file:
                                line = line.split(', ')
                                list_1.append(line)
                        with open(nm, 'w', encoding='utf8') as txt_file:
                            for line in list_1:
                                if str(line[item_type]).lower() != item_value.lower():
                                    line = ', '.join(line)
                                    txt_file.write(line)
                


readall(path)
write_1(path)

readall(path)

find_item(path)

find_item_2(path)

sort_data(path)
readall(path)


change_item(path)
readall(path)

delete_item(path)
readall(path)
