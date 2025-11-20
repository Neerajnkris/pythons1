class Recangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length *self.breadth
    def perimetere(self):
        return 2 * (self.length + self.breadth)
i1 = int(input("enter the length 1: "))
b1 = int(input("enter breadth 1: "))
r1 =  Recangle(i1, b1)
print("area of rectangle 1:", r1.area())
print("perimetere of rectangle 1:",r1.perimetere())
i2 = int(input("enter the length 2: "))
b2 = int(input("enter the breadth 2: "))
r2 = Recangle(i2, b2)
print("area of rectangle 2:", r2.area())
print("perimetere of rectangle 2:",r2.perimetere())
a1 = r1.area()
a2 = r2.area()
if a1 > a2:
    print("area of rectangle 1 is higher")
elif a1 == a2:
    print("areas are equal")
else:
    print("area of rectangle 2 is higher")