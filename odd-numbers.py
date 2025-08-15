num1= int (input("Enter first number"))
num2 = int (input("Enter second number"))
if num1 <= num2 :
    while num1 <= num2 :
        if num1 % 2 != 0:
           print(num1)
        num1= num1+1
elif num1 >= num2 :
    while num1 >= num2 :
        if num1 % 2 != 0:
           print(num1)
        num1= num1-1