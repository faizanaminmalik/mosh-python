class Point:
    def draw(self):
        print("draw")

point = Point() # This is how we create an object from a class definition
print(type(point))
print(isinstance(point, Point))