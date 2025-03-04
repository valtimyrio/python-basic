from homework_02.model import Contact, Directory


def display_menu(directory: Directory) -> None:
    print(str(directory))


def get_menu_choice():
    choice = input("Выберите интересующий пункт меню: ")
    return choice


def display_contacts(contacts: list) -> None:
    print("Просмотр контактов:")
    for contact in contacts:
        print(contact)
    print()


def get_contact_input(prompt: str = "Введите контакт (Name Phone Comment): "):
    input_str = input(prompt)
    return check_contact_input(input_str)


def check_contact_input(input_str):
    parts = input_str.split()
    if len(parts) == 0:
        print("Невозможно создать пустой контакт")
        return None
    elif len(parts) < 3:
        print("Неверно введены данные. Ожидалось: Name Phone Comment")
        return None
    return parts


def display_message(message: str) -> None:
    print(message)
