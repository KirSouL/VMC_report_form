import json
from fieldefect import get_field

def load_data_def():
    """
    Функция формирования файла с шифровкой дефектов.
    :return: возвращает краткую шифровку именованных дефектов
    """
    with open("data_defect.json", "r", encoding="utf-8") as file:
        data_def = json.load(file)

    return data_def


def min_cut():
    """
    Фунция
    :return: возвращает информацию по минимальной ширине сварного шва в зависимости от толщины стенки.
    """
    with open("data_edge_cutting_minimum.json", "r", encoding="utf-8") as file:
        edge_min_cut = json.load(file)

    return edge_min_cut


def max_cut():

    with open("data_edge_cutting_maximum.json", "r", encoding="utf-8") as file:
        edge_max_cut = json.load(file)

    return edge_max_cut


def field_def():
    """
    Функция формирования файла *.json. С результатами полевых замеров.
    :return: возвращает полевую информацию отсортированную и привязанную к ключам,
    """
    get_field()

    with open("data_field_defect.json", "r", encoding="utf-8") as file:
        defect_field = json.load(file)

    return defect_field
