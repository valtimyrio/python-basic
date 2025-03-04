import csv
import pytest

from homework_02.view import get_menu_choice, check_contact_input
from homework_02.controller import check_menu_item, InvalidMenuItemError
from homework_02.model import Contact, Directory, FileManagerRead, FileManagerWrite


@pytest.fixture()
def data():
    Dir = Directory()
    Dir.contacts = [Contact("Mary", "89120001122", "Phone"), Contact('Mike', '89230012222', 'Hi')]
    return Dir


@pytest.mark.parametrize('new_contact, expected', [
    ("Kate 89120091234 Newcontact", [Contact("Mary", "89120001122", "Phone"), Contact('Mike', '89230012222', 'Hi'), Contact("Kate", "89120091234", "Newcontact")]),
    ("", [Contact("Mary", "89120001122", "Phone"), Contact('Mike', '89230012222', 'Hi')])
])
def test_add_contact(new_contact, expected, data):
    Dir = data
    result = check_contact_input(new_contact)
    try:
        Dir.add_contact(Contact(*result))
    except:
        pass
    assert Dir.contacts == expected


@pytest.mark.parametrize('search_word, expected', [
    ('Mike', (1, Contact('Mike', '89230012222', 'Hi'))),
    ('89120001122', (0, Contact("Mary", "89120001122", "Phone"))),
    ('Nike', None)

])
def test_search_contact(search_word, expected, data):
    Dir = data
    result = Dir.search_contact(search_word)
    assert result == expected


def test_change_contact(data):
    Dir = data
    Cont_change = Contact("Lisa", "89124441177", "hello")
    Dir.change_contact(1, Cont_change)
    assert Dir.contacts == [Contact("Mary", "89120001122", "Phone"), Contact("Lisa", "89124441177", "hello")]


@pytest.mark.parametrize('search_word, expected', [
    (Contact("Mary", "89120001122", "Phone"), [Contact('Mike', '89230012222', 'Hi')]),
    (Contact("Nike", "89999999999", "Noinfo"), [Contact("Mary", "89120001122", "Phone"), Contact('Mike', '89230012222', 'Hi')])
])
def test_remove_contact(search_word, expected, data):
    Dir = data
    Dir.remove_contact(search_word)
    assert Dir.contacts == expected


def test_file_manager_read():
    with FileManagerRead("homework_03/test_data_read.csv") as result:
        assert result == [["Alice", "89121234433", "Hello"]]


def test_file_manager_write():
    C1 = Contact("Alice", "89121234433", "Hello")
    with FileManagerWrite("homework_03/test_data_write.csv", [C1]):
        pass
    file = open("homework_03/test_data_write.csv", "r", encoding='utf-8')
    result = csv.reader(file)
    assert list(result) == [["Alice", "89121234433", "Hello"]]


@pytest.mark.parametrize('menu_item, expected', [
    ("qwerty", None),
    (0, 'В меню присутствуют пункты от 1 до 8'),
    (5, 5)
])
def test_check_menu_item(menu_item, expected):
    try:
        result = check_menu_item(menu_item)
        assert result == expected

    except InvalidMenuItemError as e:
        assert str(e) == expected
