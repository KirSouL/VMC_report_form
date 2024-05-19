import math

CONST_A = 1 
CONST_B = 2
CONST_C = 3
CONST_F = 4


class CalculateDentWeld:

    def __init__(self, name, diameter, coordinate_one, coordinate_two, length, width, depth):
        self.name = name
        self.diameter = int(diameter)
        self.coordinate_on_weld = float(coordinate_one)
        self.coordinate_from_weld = abs(float(coordinate_two))
        self.length = int(length)
        self.width = int(width)
        self.depth = float(depth)
        # self.hour = None

    def is_inflection(self):
        pass


class PointFiveFive(CalculateDentWeld):
    """
    Подкласса PointFiveFive класса CalculateDentWeld,
    который осуществляет проверки для пункта 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
    """
    def __init__(self, name, diameter, coordinate_one, coordinate_two, length, width, depth):
        CalculateDentWeld.__init__(self, name, diameter, coordinate_one, coordinate_two, length, width, depth)

    def __repr__(self):
        return f"""Name(name: {self.name}, diameter: {self.diameter}, coordinate_on_weld: {self.coordinate_on_weld},
coordinate_from_weld: {self.coordinate_from_weld}, length: {self.length}, width: {self.width}, depth: {self.depth})"""
        
    def is_depth_more(self):
        """
        Метод подкласса PointFiveFive, который реализует проверку глубины вмятины
        согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
        :return: True если глубина больше 6, иначе False.
        """
        return self.depth >= 6

    def is_dent_weld(self):
        """
        Метод подкласса PointFiveFive, который реализует проверку расположения вмятины
        на стыке, согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
        :return: True если координата не "уходит" от  шва, иначе False
        """
        return self.coordinate_from_weld == 0

    # @property
    def is_minimum_distance_annular_weld(self):
        """
        Метод подкласса PointFiveFive, который реализует проверку расположения вмятины
        от кольцевого стыка, согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
        :return: True если координата меньше +- 100 от  шва, иначе False
        """
        return self.coordinate_from_weld <= 100

    # Не факт что пригодится, закомментированный кусок
    # @is_minimum_distance_annular_weld.setter
    # def is_minimum_distance_annular_weld(self, coordinate_from_annular_weld):
    #     """
    #     Метод подкласса PointFiveFive, который присваивает расположения вмятины
    #     от кольцевого стыка, согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
    #     """
    #     self.coordinate_from_weld = coordinate_from_annular_weld

    # @property
    def is_minimum_distance_longitudinal_weld(self, coord_long_dent):
        """
        Метод подкласса PointFiveFive, который реализует проверку расположения вмятины
        от продлольного стыка, согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
        :return: True если координата меньше +- 50 от  шва, иначе False
        """
        return coord_long_dent <= 50

    # Не факт что пригодится, закомментированный кусок
    # @is_minimum_distance_longitudinal_weld.setter
    # def is_minimum_distance_longitudinal_weld(self, coordinate_from_longitudinal_weld):
    #     """
    #     Метод подкласса PointFiveFive, который присваивает расположения вмятины
    #     от продлольного стыка, согласно пункту 5.5 НТД (СТО Газпром 27.3-2.2-006-2023).
    #     """
    #     self.coordinate_from_weld = coordinate_from_longitudinal_weld


class PointSixFour(CalculateDentWeld):
    """Подкласс, который реализует оценку вмятины на стыке по п. 6.4 НТД (СТО Газпром 27.3-2.2-006-2023)"""

    def __init__(self, name, diameter, coordinate_one, coordinate_two, length, width, depth, actual_thickness):
        CalculateDentWeld.__init__(self, name, diameter, coordinate_one, coordinate_two, length, width, depth)
        self.thickness = float(actual_thickness)

    def __repr__(self):
        return (f"Name(name: {self.name}, diameter: {self.diameter}, coordinate_on_weld: {self.coordinate_on_weld}"
                f", coordinate_from_weld: {self.coordinate_from_weld}, length: {self.length}, width: {self.width},"
                f" depth: {self.depth}, thickness: {self.thickness})")
    
    def two_percent(self):
        """
        Метод подкласса PointSixFour выполняющий проверку безусловности отбраковки вмятины на стыке.
        :return: возвращает True если глубина вмятины больше или равна 2% от диаметра трубы, иначе False
        """
        two_percent = self.diameter * 2 / 100

        if self.depth <= two_percent:
            return two_percent, False
        return two_percent, True

    def calculete_deformation(self, input_type_dent):
        """
        Метод подкласса PointSixFour, который производит расчет деформации
        и оценивает эквивалентную деформацию в допустимых значениях.
        :return: True возвращается в том случае, если расчетная величина эквивалентной
                 деформации больше 6%, иначе False.
        """

        pipe_radius = self.diameter / 2

        """
        В головной программе придумать условия выбора, сюда передать результат выбора
        (в интерфейсе этот пункт реализовать как расскрыввающийся список).
        """
        if input_type_dent == "плавная":
            radius_one = (self.diameter ** 2 + (self.length / CONST_B) ** 2) / (CONST_B * self.diameter)
            radius_two = (self.diameter ** 2 + (self.width / CONST_B) ** 2) / (CONST_B * self.diameter)
        else:
            ratio_one = CONST_C * (math.pi ** 2) - CONST_F * ((self.length / pipe_radius) ** 2)
            radius_one = - (self.length ** 2) / (self.diameter * ratio_one)
            radius_two = (self.width ** 2) / (CONST_C * math.pi ** 2 * self.diameter)

        # deformation_bending_circumferential =
        e_one = (self.thickness / CONST_B) * ((CONST_A / pipe_radius) - (CONST_A / radius_one))
        # deformation_bending_longitudinal =
        e_two = (self.thickness * CONST_A) / (CONST_B * radius_two)
        # deformation_stretching_longitudinal =
        e_three = (CONST_A / CONST_B) / ((self.diameter / self.width) ** 2)

        sum_one = e_two + e_three
        sum_two = e_one * sum_one + sum_one ** 2
        deformation_sum = (CONST_B / math.sqrt(CONST_C)) * math.sqrt((e_one ** 2 + sum_two))

        if deformation_sum >= 6:
            return deformation_sum
        return deformation_sum
        
# Ниже тест куска.
# dent = PointSixFour("Вмятина", 1020, 520, 50, 100, 80, 11, 12)
# print(dent.__repr__())
#
# if dent.calculete_deformation()[1] is True:
# print(f"Глубина вмятины меньше 2% от {dent.diameter}, эквивалентная деформация {round(dent.calculete_deformation()[0], 2)} > 6%"
#           f"Результат оценки 'Вырезать'")
# else:
#     print(f"Глубина вмятины меньше 2% от {dent.diameter}, эквивалентная деформация {round(dent.calculete_deformation()[0], 2)} < 6%"
#           f"Результат оценки 'Годен'")

