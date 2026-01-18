class ParentCalculator:
    # default class variable or constructor without parameters
    num = 100

    # parameterized constructor and instance variables
    def __init__(self, a, b):
        # instance variables
        self.firstNumber = int(a)
        self.secondNumber = int(b)
        print("I am called Automatically when obj is created")

    def get_data(self):
        print("I am now executing as a method in a class")

    def addition(self):
        return self.firstNumber + self.secondNumber + ParentCalculator.num


# Creating object for class
obj = ParentCalculator(20, 30)
obj.get_data()
print(obj.num)

# Addition
obj2 = ParentCalculator(10, 20)
result = obj2.addition()
print("Addition is:", result)
