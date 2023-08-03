import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def calc_perimeter(self):
    perim = self.a + self.b + self.c
    print("Consider me implemented", perim)
    return perim

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
def calc_perimeter(self):
    perim = 2 * (self.a + self.b)
    print("Consider me implemented", perim)
    return perim

class Square(Shape):
    def __init__(self, a):
        self.a = a
    
def calc_perimeter(self):
    perim = 4 * self.a
    print("Consider me implemented", perim)
    return perim



