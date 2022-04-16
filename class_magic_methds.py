class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})" # We modify behavious of this magic method to return formatted data

    def draw(self):
        print(f'Point ( {self.x} , {self.y} )')

point = Point(1,2)
print(point)
# without defining __str__() methos this returns <Class object HJH&hj67>