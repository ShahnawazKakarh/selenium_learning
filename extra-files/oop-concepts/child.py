from parent import ParentCalculator


class ChildCalculator(ParentCalculator):
    num2 = 200

    def __init__(self):
        ParentCalculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num + self.num2 + self.addition()


obj = ChildCalculator()
print(obj.get_complete_data())
