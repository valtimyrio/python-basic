from model import Contact, Directory


def display_menu(directory: Directory) -> None:
    print(str(directory))


def get_menu_choice():
    try:
        choice = int(input("Выберите интересующий пункт меню: "))
        return choice
    except ValueError:
        print("Введенное значение не является числом\n")
        return None


def display_contacts(contacts: list) -> None:
    print("Просмотр контактов:")
    for contact in contacts:
        print(contact)
    print()


def get_contact_input(prompt: str = "Введите контакт (Name Phone Comment): "):
    input_str = input(prompt)
    parts = input_str.split()
    if len(parts) < 3:
        print("Неверно введены данные. Ожидалось: Name Phone Comment")
        return None
    return parts


def display_message(message: str) -> None:
    print(message)
