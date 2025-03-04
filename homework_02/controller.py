from model import Directory, Contact, FileManagerRead, FileManagerWrite
from view import display_menu, get_menu_choice, display_contacts, get_contact_input, display_message


class InvalidMenuItemError(Exception):
    """Класс ошибки выбора пункта меню"""
    def __init__(self, menu_item, message="В меню присутствуют пункты от 1 до 8"):
        self.menu_item = menu_item
        self.message = message
        super().__init__(self.message)


def check_menu_item(menu_item: int) -> None:
    if menu_item < 1 or menu_item > 8:
        raise InvalidMenuItemError(menu_item)


def main():
    directory = Directory()
    exit_flag = False

    while not exit_flag:
        display_menu(directory)
        choice = get_menu_choice()
        if choice is None:
            continue
        try:
            check_menu_item(choice)
        except InvalidMenuItemError as e:
            display_message(f"Ошибка: {e}")
            continue

        directory.menu_item = choice

        if choice == 1:
            if directory.file_open:
                display_message("Требуется сначала сохранить открытый файл\n")
            else:
                try:
                    with FileManagerRead("data.csv") as file_data:
                        directory.file_open = True
                        directory.contacts.clear()
                        for contact_info in file_data:
                            directory.contacts.append(Contact(*contact_info))
                    display_message("Файл открыт\n")
                except Exception as e:
                    display_message(f"Ошибка при открытии файла: {e}")
        elif choice == 8:
            exit_flag = True
        elif directory.file_open:
            if choice == 2:
                try:
                    with FileManagerWrite("data.csv", directory.contacts):
                        directory.file_open = False
                    display_message("Запись в файл закончена\n")
                    directory.contacts.clear()
                except Exception as e:
                    display_message(f"Ошибка при сохранении файла: {e}")
            elif choice == 3:
                display_contacts(directory.contacts)
            elif choice == 4:
                parts = get_contact_input("Введите контакт (Name Phone Comment): ")
                if parts:
                    try:
                        new_contact = Contact(*parts)
                        directory.add_contact(new_contact)
                        display_message("Новый контакт успешно создан\n")
                    except Exception:
                        display_message("Новый контакт не создан. Неверно введены данные\n")
            elif choice in (5, 6, 7):
                search_word = input("Введите слово для поиска/изменения/удаления контакта: ")
                search_res = directory.search_contact(search_word)
                if search_res:
                    index, found_contact = search_res
                    if choice == 5:
                        display_message(f"Найден контакт: {found_contact}")
                    elif choice == 6:
                        display_message(f"Изменить контакт: {found_contact}")
                        parts = get_contact_input("Введите новый контакт (Name Phone Comment): ")
                        if parts:
                            try:
                                new_contact = Contact(*parts)
                                directory.change_contact(index, new_contact)
                                display_message("Контакт изменен\n")
                            except Exception:
                                display_message("Не удалось изменить контакт")
                    elif choice == 7:
                        directory.remove_contact(found_contact)
                        display_message(f"Удален контакт: {found_contact}\n")
                else:
                    display_message("Контакт не найден\n")
        else:
            display_message("Перед работой с файлом следует его открыть\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма была прервана\n")