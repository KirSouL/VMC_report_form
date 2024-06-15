import openpyxl
import json
import os
import datetime
# import copy
# import pandas

# control = pandas.read_excel('Дефектовка.xlsx')
# print(control.head())


def open_file():
    # Расположение файла с данными о приборах и их поверке
    file_location = os.path.abspath('../Данные по приборам.xlsx')
    # Загрузка файла эксель -- 'Данные по приборам'
    workbook_data_device = openpyxl.load_workbook(file_location)
    # Активация первого листа эксель файла
    # worksheet_data_device = workbook_data_device.active
    return workbook_data_device.active


def data_device():
    """
    Функция формирует json файл из файла Excel, в котором расположена инфа по приборам
    с датами актуальной поверки. Файл Excel формируются пользователем.
    :return list_device: возвращает список словарей -- Пример --
                        [{
                        "key_number": "1",
                        "device": "Наименование прибора и зав. номер",
                        "verification_date": "10.04.2025 г."
                        }]
    """
    list_device = []
    dict_device = {}

    for row in open_file().values:
        for value in row:
            if type(value) is datetime.datetime:
                date = value.date()
                date = date.strftime("%d.%m.%Y")
                dict_device['verification_date'] = date
            elif type(value) is str:
                dict_device['device'] = value
            else:
                dict_device['key_number'] = value
        list_device.append(dict_device.copy())

    return list_device
            

def get_json():
    """
    Функция генерирует json файл.
    """
    with open('../device.json', 'w', encoding='utf-8') as file:
        json.dump(data_device(), file, indent=4)
    # Строчки ниже для проверки результата
    with open('../device.json', 'r') as file:
        print(json.load(file))


def get_control():
    pass
