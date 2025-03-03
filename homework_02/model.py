import csv
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Contact:
    """Датакласс контакта"""

    name: str
    phone: str
    comment: str

    def __str__(self):
        return f"{self.name} {self.phone} {self.comment}"


class Directory:
    """Класс справочника, содержащий контакты, состояние файла и меню"""

    def __init__(self) -> None:
        self.contacts = []  # Список контактов
        self.file_open = False
        self.menu_item = None
        self._menu = (
            "МЕНЮ:\n"
            "1) Открыть файл\n"
            "2) Сохранить файл\n"
            "3) Показать все контакты\n"
            "4) Создать контакт\n"
            "5) Найти контакт\n"
            "6) Изменить контакт\n"
            "7) Удалить контакт\n"
            "8) Выход\n"
        )

    def __str__(self) -> str:
        return self._menu

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def remove_contact(self, contact: Contact) -> None:
        if contact in self.contacts:
            self.contacts.remove(contact)


class FileManager(ABC):
    """Абстрактный базовый класс файла"""

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    @abstractmethod
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class FileManagerRead(FileManager):
    """Класс чтения файла"""

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name, "r")

    def __enter__(self) -> list:
        self.file = open(self.file_name, self.mode, encoding='utf-8')
        reader = csv.reader(self.file)
        return list(reader)


class FileManagerWrite(FileManager):
    """Класс записи файла"""

    def __init__(self, file_name: str, data: list) -> None:
        super().__init__(file_name, "w")
        self.data = data

    def __enter__(self) -> None:
        self.file = open(self.file_name, self.mode, encoding='utf-8')
        for line in self.data:
            self.file.write(f"{line.name},{line.phone},{line.comment}\n")