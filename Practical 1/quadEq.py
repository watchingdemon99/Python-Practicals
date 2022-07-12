# Program to find roots of Quadratic Equations

a = int(input("Enter the coefficient x^2 "))
b = int(input("Enter the coefficient x "))
c = int(input("Enter the constant "))

det = (b*b - 4 * a * c) ** (0.5)
r1 = (-b + det)/(2*a)
r2 = (-b - det)/(2*a)

print(f"The roots of the equation are {r1}  and {r2}")

