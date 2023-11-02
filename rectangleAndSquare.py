class Rectangle:

    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth
    
    def getArea(self):
        area = self.length * self.breadth
        print("Finding area of the rectangle")
        return area

class Square(Rectangle):

    # def __init__(self, side) -> None:
    #     self.side= side
    
    def getArea(self):
        area = self.length * self.length
        print("Finding area of the square")
        return area

square1 = Square(4,4)
print(square1.getArea())

rect1 = Rectangle(3,8)
print(rect1.getArea())
