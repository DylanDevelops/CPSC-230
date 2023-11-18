import math

class Shapes():
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length


    def CalculateArea(self):
        if self.sides == 3:
            return((math.sqrt(3)/4) * (self.length ** 2))
        elif self.sides == 4:
            return(self.length * self.length)
        elif self.sides == 6:
            return((3 * math.sqrt(3) * (self.length ** 2))/(2))

    def CalculatePerimeter(self):
        return(self.length * self.sides)


triangle = Shapes(3, 10)
square = Shapes(4, 10)
hexagon = Shapes(6, 10)

print("--Triangle--")
print(triangle.CalculateArea())
print(triangle.CalculatePerimeter())
print("--Square--")
print(square.CalculateArea())
print(square.CalculatePerimeter())
print("--Hexagon--")
print(hexagon.CalculateArea())
print(hexagon.CalculatePerimeter())