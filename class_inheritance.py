class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("Eat")

#Animal: Parent class or base class
#Mammal: Child class or sub class
class Mammal(Animal):
    def walk(self):
        print ("walk")

class Fish(Animal):
    def swim(self):
        print("Swim")

cat = Mammal()
cat.eat()
cat.walk()
print(cat.age)

tuna = Fish()
tuna.swim()

print(isinstance(cat, Mammal))
#Every class is an instance of object class
print(isinstance(cat, object))