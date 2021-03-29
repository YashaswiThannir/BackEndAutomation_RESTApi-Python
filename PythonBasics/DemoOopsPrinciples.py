# classes are user defined prototype or a blueprint
# constructor is a method which is automatically created when you create a object for any class
# the variables declared inside a class are called class variables.
# the variables created inside constructor are called instance variables.
# instance variables keep changing for every object creation (here obj1, obj2). Class variables remain constant.
# self keyword is mandatory for calling variable names into methods
# instance variables are attached to the object, class variables are not attached to the object

class Calculator:
    num = 100   # class variable

    # constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I execute when a object is created for class")

    def getData(self):
        print("I'm a method in class")

    def AddIntegers(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj1 = Calculator(2, 3)  # syntax to create object in python for a class
obj1.getData()
print(obj1.num)
print(obj1.AddIntegers())

obj2 = Calculator(4, 5)  # syntax to create object in python for a class
obj2.getData()
print(obj2.num)
print(obj2.AddIntegers())

