class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


# Create an instance with values 10 and 5
calculator = BasicCalculator(10, 5)

print("Addition:", calculator.addition())
print("Subtraction:", calculator.subtraction())
print("Multiplication:", calculator.multiplication())
print("Division:", calculator.division())
