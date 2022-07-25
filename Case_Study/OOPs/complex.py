'''Q.1 Write a python program to perform the following operations on complex numbers by
creating a class complex_number. Create two objects c1 and c2.
a. Addition
b. Subtraction
c. Multiplication
d. Check if two complex numbers are equal or not
e. Check if c1>=c2
f. Check if c1==c2
Perform these operations using operator overloading in python'''


class ComplexNumber:

    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.imaginary = complex_part
        self.number = f"{self.real_part}+{self.imaginary}i"

    def display(self):
        print(self.number)

    def __add__(self, other):
        return f"{self.real_part + other.real_part} + {self.imaginary + other.imaginary}i"

    def __sub__(self, other):
        if self.imaginary - other.imaginary >= 0:
            return f"{self.real_part - other.real_part} + {self.imaginary - other.imaginary}i"
        else:
            f"{self.real_part + other.real_part} - {(self.imaginary + other.imaginary) * -1}i"

    def __mul__(self, other):
        return f"{self.real_part * other.real_part - self.imaginary * other.imaginary} + " \
               f"{self.real_part * other.imaginary + self.imaginary * other.real_part}i "

    def __eq__(self, other):
        if self.real_part == other.real_part and self.imaginary == other.imaginary:
            return True
        else:
            return False

    def __le__(self, other):
        return self.real_part <= other.real_part and self.imaginary <= other.imaginary

    def __ge__(self, other):
        return self.real_part >= other.real_part and self.imaginary >= other.imaginary


c1 = ComplexNumber(5, 10)
c2 = ComplexNumber(10, 5)

c1.display()
c2.display()

print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")
print(f"c1 * c2 = {c1 * c2}")
print(f"c1 <= c2 : {c1 <= c2}")
print(f"c1 >= c2: {c1 >= c2}")
print(f"c1 == c2: {c1 == c2}")