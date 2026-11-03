"""vector objects to work with"""


class Vector():

        DIMENSION=2

        def __init__(self, x,y):
                self.x = x
                self.y = y

        def __repr__(self):
            return "Vector({x},{y})".format(x=self.x, y=self.y)

        def __add__(self, other):
                self.x += other.x
                self.y += other.y

                return self

