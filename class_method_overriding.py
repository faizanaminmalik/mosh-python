class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("Eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__() # Call Base class constructor to init age attribute
        self. weight = 2
    def walk(self):
        print ("walk")

class Fish(Animal):
    def __init__(self):
        super().__init__() # Call Base class constructor to init age attribute
        self. length = 3
    def swim(self):
        print("Swim")

tuna = Fish()
print(tuna.length)
print(tuna.age)