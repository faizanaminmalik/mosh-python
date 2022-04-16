class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f'Point ( {self.x} , {self.y} )')

point1 = Point(1,2)
point2 = Point(1,2)
point3 = point1 + point2 # We can add elements of 2 classes by defining __add()__magic method
print(point3.x, point3.y)
