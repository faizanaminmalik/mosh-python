class Point:
    default_color = "red"
    def __init__(self, x, y): # constructor to initalize values of variables of class
        self.x = x
        self.y = y

    @classmethod # Decorator to tell python this is a class method
    def zero(cls): #cls is a class reference cls is a naming convention
        return cls(0, 0)

    def draw(self): #self is a reference to current object. using self, we can access attributes and call methods
        print(f'Point ( {self.x} , {self.y} )')

#point = Point(1,2) #creating an object from class Point
point = Point.zero()
point.draw()