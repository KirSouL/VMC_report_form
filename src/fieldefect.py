import openpyxl
import json
import os


def open_file_field():
    """
    Функция открытия файла Excel
    :return: аквтивация первого листа файла Excel
    """
    file_field = os.path.abspath('../Данные.xlsx')
    workbook = openpyxl.load_workbook(file_field)
    worksheet_one = workbook.worksheets[0]

    return worksheet_one


def list_defect():
    """
    Функция преобразования данных из формата Excel в формат списка с вложенными словарями.
    :return: возвращается список с набором словарей для формирования файла *.json
    """
    list_ = []
    dict_ = {}
    list_t = []

    for row in open_file_field().values:
        for item in row:
            list_.append(str(item))

            for value in range(len(list_)):
                if value > 9:
                    if value % 10 == 0:
                        dict_["number_weld"] = list_[value]

                    if value % 10 == 1:
                        dict_["diameter"] = list_[value]

                    if value % 10 == 2:
                        dict_["thickness"] = list_[value]

                    if value % 10 == 3:
                        dict_["coordinate_zero"] = list_[value]

                    if value % 10 == 4:
                        dict_["coordinate_from_weld"] = list_[value]

                    if value % 10 == 5:
                        dict_["name_defect"] = list_[value].lower()

                    if value % 10 == 6:
                        dict_["length"] = list_[value]

                    if value % 10 == 7:
                        dict_["width_min"] = list_[value]

                    if value % 10 == 8:
                        dict_["width_max"] = list_[value]

                    if value % 10 == 9:
                        dict_["depth"] = list_[value]

        list_t.append(dict_.copy())

    return list_t


def get_field():
    """Функция генерирует файл *.json из списка полученного из функции list_defect()"""
    with open('../data_field_defect.json', 'w', encoding='utf-8') as file:
        json.dump(list_defect(), file, indent=4)
