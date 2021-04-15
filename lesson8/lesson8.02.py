class DivisionByZero:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    @staticmethod
    def divide(arg_1, arg_2):
        try:
            return (arg_1 / arg_2)
        except:
            return (f"Делить на ноль нельзя!")


div = DivisionByZero(10, 100)
print(DivisionByZero.divide(200, 0))
print(DivisionByZero.divide(152, 0.36))
print(div.divide(100, 0))
