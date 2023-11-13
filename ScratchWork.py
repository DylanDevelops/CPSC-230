class DylanMath():
    import math

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        return a / b

    def FDivide(self, a, b):
        return a // b

    def IsEven(self, a):
        if a % 2 == 0:
            return True
        else:
            return False



math = DylanMath()

print(math.Multiply(10, 20))
print(math.IsEven(10))