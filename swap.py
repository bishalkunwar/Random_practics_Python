x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))

print("Before swap: ")
print("x is : ", x, " and y is : ", y)

x = x+y
y = x-y
x = x-y

print("After swap: ")
print("x is : ", x, " and y is : ", y)