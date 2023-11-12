class Rectangle:

    def __init__(self, side_1, side_2=None):
        self.side_1 = side_1
        self.side_2 = side_1 if side_2 is None else side_2

    def get_perimeter(self):
        return (self.side_1 + self.side_2) * 2

    def get_area(self):
        return self.side_1 * self.side_2

    def __add__(self, other):
        return Rectangle(self.get_perimeter() + other.get_perimeter())

    def __sub__(self, other):
        return Rectangle(abs(self.get_perimeter() - other.get_perimeter()))

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()
