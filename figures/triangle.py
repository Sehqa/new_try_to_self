import uuid
import math


class Triangle:

    def __init__(self, name='TEST', first_side=None, second_side=None, third_side=None, first_corner=None, second_corner=None, third_corner=None):
        if (first_side or second_side or third_side) is None:
            raise ValueError
        elif (first_side or second_side or third_side) < 0:
            raise ValueError
        else:
            self.guid = uuid.uuid4()
            self.name = name
            self.type = 'Треугольник'
            self.first_side = first_side
            self.second_side = second_side
            self.third_side = third_side
            self.first_corner = first_corner
            self.second_corner = second_corner
            self.third_corner = third_corner
            self.square = self.calculate_square()

    def calculate_square(self):
        return math.sqrt(((self.first_side + self.second_side + self.third_side) / 2) * (
                ((self.first_side + self.second_side + self.third_side) / 2 - self.first_side) * (
                (self.first_side + self.second_side + self.third_side) / 2 - self.second_side) * (
                        (self.first_side + self.second_side + self.third_side) / 2 - self.third_side)))
