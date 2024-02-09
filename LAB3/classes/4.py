class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((abs(self.x - other_point.x))**2 + (abs(self.y - other_point.y))**2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show() 

point1.move(3, 5)
point1.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

