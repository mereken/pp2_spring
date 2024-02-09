class Shape:
    length = 0
        
    def area(self):
        print(self.length*self.length)
        
class Square(Shape):
    def __init__(self, length):
        self.length=length
        

qwe = Square(5)

qwe.area()