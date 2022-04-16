class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def draw(self):
        print(f'Point ( {self.x} , {self.y} )')

point = Point(1,2)
point2 = Point(1,2)
print(point == point2) # Only be defining __EQ__ magic method we can compare 2 classes and it returns true as both r same

point3 = Point(3,4)
print(point2 < point3) # Without defining __GT__ magic method we couldnt compare lessthan/ greaterthan between elements of 2 classes
