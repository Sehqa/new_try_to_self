import uuid


class Circle:

    def __init__(self, name='TEST', radius=None):
        if radius is None:
            raise ValueError
        elif (radius) <0:
            raise ValueError
        else:
            self.guid = uuid.uuid4()
            self.name = name
            self.type = 'Круг'
            self.radius = radius
            self.diameter = radius * 2
            self.square = 2 * 3.14 * radius
