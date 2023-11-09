class Rectangle:

    def __init__(self, side_1, side_2=None):
        self.side_1 = side_1
        self.side_2 = side_1 if side_2 is None else side_2

    def get_perimeter(self):
        return (self.side_1 + self.side_2) * 2

    def get_area(self):
        return self.side_1 * self.side_2
