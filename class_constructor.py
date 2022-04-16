class Point:
    default_color = "red" # Class level attribute. Same across all objects
    def __init__(self, x, y): # constructor to initalize values of variables of class
        self.x = x
        self.y = y

    def draw(self): #self is a reference to current object. using self, we can access attributes and call methods
        print(f'Point ( {self.x} , {self.y} )')
point = Point(1,2) #creating an object from class Point
point.draw()
print(point.default_color)
print(Point.default_color)

Point.default_color = "Yellow"
print(point.default_color)
print(Point.default_color)