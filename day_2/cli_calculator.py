num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("Select the operator(+,-,*,/,%):")
if(operator=='+'):
    result = num1+num2
    print(f"Result is {result}")
elif(operator=='-'):
    result = num1-num2
    print(f"Result is {result}")
elif(operator=='*'):
    result = num1*num2
    print(f"Result is {result}")
elif(operator=='/' and num2!=0):
    result = num1/num2
    print(f"Result is {result}")
elif(operator=='/' and num2==0):
    print(f"Cannot divide by zero")
elif(operator=='%' and num2!=0):
    result = num1%num2
    print(f"Result is {result}")
elif(operator=='%' and num2==0):
    print(f"Cannot divide by zero")
elif(f"{num1} or {num2} is not a number"):
    print("Invalid input")
else:
    print("Invalid operator")