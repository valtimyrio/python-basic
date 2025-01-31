import csv


def menu():
    return input("Выберите интересующий пункт меню:\n1)Открыть файл\n2)Сохранить файл\n3)Показать все контакты\n4)Создать контакт\n5)Найти контакт\n6)Изменить контакт\n7)Удалить контакт\n8)Выход\n\n")


exit_flag = False
file_open = False


def open_file():
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    print("Файл открыт\n")
    return data


def save_file(data):
    global file_open
    with open('data.csv', 'w', encoding='utf-8') as file:
        for line in data:
            file.write(",".join(line))
            file.write("\n")
    file_open = False
    print("Файл сохранен\n")


def view_contacts(data):
    for line in data:
        print(*line)
    print()


def create_contact(data):
    new_contact = input('Введите "Name Phone Comment": ')
    new_contact_list = new_contact.split()
    if len(new_contact_list) != 3:
        print("Новый контакт не создан. Неверно введены данные\n")
    else:
        data.append(new_contact_list)
        print("Новый контакт успешно создан\n")


def find_contact(data):
    word_to_find = input("Введите слово для поиска: ")
    for line in data:
        if word_to_find in line:
            print(*line)
    print()


def change_contact(data):
    change_index = None
    word_to_change = input("Введите слово, содержащееся в строке для изменения: ")
    for list_index in range(len(data)):
        if word_to_change in data[list_index]:
            change_index = list_index
            break
    if change_index is not None:
        new_contact = input('Введите "Name Phone Comment": ')
        change_contact_list = new_contact.split()
        if len(change_contact_list) != 3:
            print("Новый контакт не был изменен. Неверно введены данные\n")
        else:
            data[change_index] = change_contact_list
            print("Новый контакт успешно создан\n")
    else:
        print('Нет записи для изменения\n')


def delete_contact(data):
    delete_con = None
    word_to_delete = input("Введите слово, содержащееся в строке для удаления: ")
    for list_index in range(len(data)):
        if word_to_delete in data[list_index]:
            delete_con = data.pop(list_index)
            break
    if delete_con is not None:
        print(f'Удалена запись {" ".join(delete_con)}\n')
    else:
        print('Нет записи для удаления\n')


def exit_func():
    global exit_flag
    exit_flag = True


menu_dict = {1: open_file, 2: save_file, 3: view_contacts, 4: create_contact, 5: find_contact, 6: change_contact, 7: delete_contact, 8: exit_func}

while not exit_flag:

    menu_item = menu()
    if not menu_item.isdigit() or int(menu_item) > 8 or int(menu_item) < 1:
        print("Неверно выбран пункт меню\n")
    else:
        if menu_item == "1":
            data = open_file()
            file_open = True
        elif menu_item == "8":
            exit_func()
        elif file_open:
            func_name = menu_dict[int(menu_item)]
            func_name(data)
        else:
            print("Перед работой с файлом следует его открыть\n")
