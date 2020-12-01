#program to calculate the area of a traingle.

#importing math library
import math

a = int(input("enter the area of first side:"))
b = int(input("enter the area of second side:"))
c = int(input("enter the area of third side:"))

s = (a+b+c)/2
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("the area of a traingle is %0.2f:" %area)