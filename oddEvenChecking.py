#WAP   to take two input value
# from user and check the value is odd or even
# if even then add the 5 multiple until its sum being 100.

#Solution:

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

#Global variables declaration:
sum = 0
remainder = 0
c = 5

#Checking odd and even of intigers
if input1 % 2 == 0 and input2 % 2 == 0:
    sum = input1 + input2

#apply the condition to get sum equals to 100.
    while sum <= 100:
        sum = sum+5
        c = c+5
        if sum > 100:
            remainder = sum - 100
    sum = sum - remainder
    print("The even numbers are ", input1," ", input2," and the sum reached to the ",sum)
else:
    print("The numbers {0} and {1} has odd integrity and no further processing required." .format(input1, input2))
