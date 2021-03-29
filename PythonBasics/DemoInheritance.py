# Inheritance is nothing but acquiring properties(variables & methods))of parent class to child class
# if you have a parent constructor in parent class which is not default then call the parent constructor in child constructor
from PythonBasics.DemoOopsPrinciples import Calculator


# inheriting parent class Calculator to child class
class ChildImpl(Calculator):
    num2 = 250

    def __init__(self):
        Calculator.__init__(self, 2, 4)

    def getAllData(self):
        return self.num2 + self.num + self.AddIntegers()


obj = ChildImpl()
print(obj.num2)
print(obj.getAllData())
