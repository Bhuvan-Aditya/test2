class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.num + other.num)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Number' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.num - other.num)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Number' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Number' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.num == 0:
                raise ZeroDivisionError("Division by zero")
            return Number(self.num / other.num)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Number' and '{}'".format(type(other).__name__))

# Demonstration
num1 = Number(10)
num2 = Number(5)

# Addition
result_addition = num1 + num2
print("Addition:", result_addition)

# Subtraction
result_subtraction = num1 - num2
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = num1 * num2
print("Multiplication:", result_multiplication)

# Division
result_division = num1 / num2
print("Division:", result_division)

# Combined expression
result_combined = num1 + num2 - num2 * num1 / num2
print("Combined expression:", result_combined)
