class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")
class Manager(Employee, Person):
    pass

mg1 = Manager()
mg1.greet() # Employee Greet will be called as employee is mentioned first in class statement -> class Manager(Employee, Person):