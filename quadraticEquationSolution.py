
import cmath

s1 =  int(input("Enter the value of side1: "))
s2 =  int(input("Enter the value of side2: "))
s3 =  int(input("Enter the value of side3: "))

d = (s2 ** 2 - 4 * s1 * s3)/2*s1

x1 = (-s2 - cmath.sqrt(d)) / (2 * s1)
x2 = (-s2 + cmath.sqrt(d)) / (2 * s1)

print("The value of x1 = {0} and x2 = {1}" .format(x1, x2))