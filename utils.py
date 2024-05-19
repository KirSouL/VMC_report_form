import CalculateDentSeam
import json
import math


def load_file():
    """
    Функция загрузки файла с полевыми данными
    :return: возвращает прочитанный файл json
    """
    with open('data_field_defect.json', 'r') as file:
        load_field = json.load(file)

    return load_field


def download_calc_dent():
    """
    Функция обработки дефекта типа "вмятина"
    :return:
    """
    for item in load_file():
        if item.get("name_defect") == "вмятина":
            user_type_calc = str(input('Выберите раздел расчета для вмятины (5.5 или 6.4): '))

            nd, dim, cz = item.get("name_defect"), item.get("diameter"), item.get("coordinate_zero")
            cfw, lh, wm = item.get("coordinate_from_weld"), item.get("length"), item.get("width_max")
            dh = item.get("depth")

            if user_type_calc == '5.5':
                # return тут экземпляр класса 'вмятины' CalculateDentSeam.PointFiveFive()
                dent = CalculateDentSeam.PointFiveFive(nd, dim, cz, cfw, lh, wm, dh)
                print(dent)
                print(dent.is_dent_weld())
                print(dent.is_depth_more())
                print(dent.is_minimum_distance_annular_weld())
                print(conversion_to_hours(cz, dim))
            else:
                ts = item.get("thickness")
                dent = CalculateDentSeam.PointSixFour(nd, dim, cz, cfw, lh, wm, dh, ts)
                crit_two = dent.two_percent()[1]
                if crit_two is True:
                    print(crit_two)
                    print(conversion_to_hours(cz, dim))
                else:
                    type_dent = input("Тип вмятины (плавная или с углублением): ")
                    print(dent.calculete_deformation(type_dent))
                    print(conversion_to_hours(cz, dim))

                # return тут экземпляр класса 'вмятины' CalculateDentSeam.PointSixFour()


def conversion_to_hours(*args):
    """
    Функция осуществляющая перевод координаты из 'мм' в 'часы'.
    :return: возвращает значение сконвертированного часа
    """
    if float(args[0]) < 0:
        coordinate_on_weld = int(args[1]) * math.pi + float(args[0])
        hour = round((coordinate_on_weld / (int(args[1]) * math.pi / 12)), 1)
        return hour
    else:
        hour = round((float(args[0]) / (int(args[1]) * math.pi / 12)), 1)
        return hour


def axial_fracture():
    """
    Функция расчета перелома осей
    :return: возвращается значение угла, информации о дефекте, часовой ориентации
    """
    for item in load_file():
        if item.get("name_defect") == "перелом осей":
            user_len = int(input("Введите размер площадки замера, мм: "))
            tan_angle = float(item.get("depth")) / user_len
            angle = round((tan_angle * 180 / math.pi), 1)
            hour_fracture = conversion_to_hours(item.get("coordinate_zero"), item.get("diameter"))

            return angle, item, hour_fracture


one, two, three = axial_fracture()

print(one)
print(two)
print(three)

download_calc_dent()
