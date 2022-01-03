import uuid


class Square:
    def __init__(self, name='TEST', side=None):
        if side is None:
            raise ValueError
        elif (side) < 0:
            raise ValueError
        else:
            self.guid = uuid.uuid4()
            self.name = name
            self.type = 'Квадрат'
            self.side = side
            self.square = side * side
