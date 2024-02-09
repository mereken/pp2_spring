class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    def area(self):
        print(self.width*self.length)
        
        
qwe = Rectangle(4,2)

qwe.area()