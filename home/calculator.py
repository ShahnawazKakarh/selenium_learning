# Here, is the Summary:
# self.firstNumber and self.secondNumber are instance variables
# because their value is dynamic and assigned during the object creation
# while a and b are parameters of instance variable __init_
# while num is class variable because its value is static
# and self is a keyword which represents current class object
# and used to access the instance variables and methods within the class

class Calculator:
    # default class variable or constructor without parameters
    # whose scope is within the class and value is static
    num = 100

    # parameterized constructor and instance variables
    # whose scope is within the class and value is dynamic
    def __init__(self, a, b):
        # instance variables
        self.firstNumber = int(a)
        self.secondNumber = int(b)
        print("I am called Automatically when obj is created")

    def get_data(self):
        print("I am now executing as a method in a class")

    def addition(self):
        return self.firstNumber + self.secondNumber


# Constructor is one method, it is automatically called when we create obj for any class
# Creating object for class
obj = Calculator(20, 30)
obj.get_data()
print(obj.num)

# Addition
obj2 = Calculator(10, 20)
result = obj2.addition()
print("Addition is:", result)
# Subtraction
obj3 = Calculator(50, 30)
subtraction = obj3.firstNumber - obj3.secondNumber
print("Subtraction is:", subtraction)
# Multiplication
obj4 = Calculator(5, 4)
multiplication = obj4.firstNumber * obj4.secondNumber
print("Multiplication is:", multiplication)
# Division
obj5 = Calculator(40, 8)
division = obj5.firstNumber / obj5.secondNumber
print("Division is:", division)
# Modulus
obj6 = Calculator(29, 6)
modulus = obj6.firstNumber % obj6.secondNumber
print("Modulus is:", modulus)
