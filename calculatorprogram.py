num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
if operation=="+":
    sum=num1+num2
    print("The sum is", sum)
elif operation=="-":
    difference=num1-num2
    print("The difference is", difference)
elif operation=="*":
    product=num1*num2
    print("The product is", product)
elif operation=="/":
    if num2 != 0:
        quotient=num1/num2
        print("The quotient is", quotient)
    else:
        print("Error: Division by zero is not allowed.")