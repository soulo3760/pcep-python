def calculator():
    num1 = float(input('enter your first number:'))
    operator = input("enter the operator (+, -, *, /): ")
    num2 = float(input("enter the second number: "))


    if operator == "+":
        print(f'the result is : {num1 + num2}')
    elif operator == "-":
        print(f'the result is: {num1 - num2}')
    elif operator == "*":
        print(f'the result is: {num1 * num2}')
    elif operator == "/":
        if num2 != 0:
            print(f'the result is: {num1 / num2}')
        else:
            print('canno divide by zero')
    else:
        print('invalid operator')

calculator()