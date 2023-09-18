"""Первое задание.

Вам поручили написать простой парсер для значений, которые вы получаете из
внешнего API. На вход вы получаете список строк, в которых нечетные
слова - это ключи, а четные слова - это их значения. Ключи, значения которых
вы должны учитывать - id, name, last_name, age, salary, position. Остальные
ключи и их значения не должны попасть в итоговый набор данных. Ключ age и id
должен быть представлен в формате int. Ключ salary должен быть представлен в
формате Decimal.

Ограничения:
1) На вход подается информация по сотрудникам, где всегда четное количество
слов
2) Там, где нужны числовые значения, числа могут быть преобразованы к int или
Decimal без ошибок.

После парсинга вы должны получить структуру данных, описанную ниже
list[dict[str, int | str]]:
[{'id': 1, 'name': 'Ivan', 'last_name': 'Ivanov', 'age': 29,
'position': 'developer', 'salary': Decimal('10000')}, ...]

для тестирования запустить pytest 1_task/test.py
"""
import os
import types
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'
EMPLOYEE_INFO_DISPATCH_DICT = types.MappingProxyType({
    'id': int,
    'name': str,
    'last_name': str,
    'age': int,
    'salary': Decimal,
    'position': str,
})


def read_file(path: str) -> str:
    """Функция чтения файла.

    Args:
        path: путь до файла

    Returns:
        прочитанный файл в виде строки
    """
    with open(path, 'r') as file_with_data:
        employees_data = file_with_data.read()
    return employees_data


def get_employees_info() -> list[str]:
    """Внешнее API, возвращающее список строк с данными по сотрудникам.

    Returns:
        список строк с данными по сотрудникам
    """
    return read_file(
        os.path.join(
            BASE_DIR,
            '1_task',
            'input_data.txt',
        ),
    ).split(SPLIT_SYMBOL)


def correct_employee_info(employee_info: str) -> dict[str, int | str]:
    """Функция корректировки данных по шаблону.

    Args:
        employee_info: строка данных о сотруднике.

    Returns:
        Словарь, оформленный по шаблону.
    """
    employee_info_list = employee_info.split()
    return {
        key: EMPLOYEE_INFO_DISPATCH_DICT[key](employee_info_list[index + 1])
        for index, key in enumerate(employee_info_list)
        if key in EMPLOYEE_INFO_DISPATCH_DICT.keys()
    }


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция приведения данных к стандартизированному виду.

    Returns:
        стандартизированный вид записи информации о сотрудниках
    """
    employees_info = get_employees_info()
    parsed_employees_info = []

    for employee_info in employees_info:
        parsed_employees_info.append(
            correct_employee_info(employee_info),
        )
    return parsed_employees_info
