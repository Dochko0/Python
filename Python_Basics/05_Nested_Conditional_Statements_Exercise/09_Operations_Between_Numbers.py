num1 = float(input())
num2 = float(input())
operator = input()

if operator == '+':
    result = num1 + num2
    if result % 2 == 0:
        print(f'{num1:.0f} + {num2:.0f} = {result:.0f} - even')
    else:
        print(f'{num1:.0f} + {num2:.0f} = {result:.0f} - odd')
elif operator == '-':
    result = num1 - num2
    if result % 2 == 0:
        print(f'{num1:.0f} - {num2:.0f} = {result:.0f} - even')
    else:
        print(f'{num1:.0f} - {num2:.0f} = {result:.0f} - odd')
elif operator == '*':
    result = num1 * num2
    if result % 2 == 0:
        print(f'{num1:.0f} * {num2:.0f} = {result:.0f} - even')
    else:
        print(f'{num1:.0f} * {num2:.0f} = {result:.0f} - odd')
elif operator == '/':
    if num2 == 0:
        print(f'Cannot divide {num1:.0f} by zero')
    else:
        result = num1 / num2
        print(f'{num1:.0f} / {num2:.0f} = {result:.2f}')
elif operator == '%':
    if num2 == 0:
        print(f'Cannot divide {num1:.0f} by zero')
    else:
        result = num1 % num2
        print(f'{num1:.0f} % {num2:.0f} = {result:.0f}')
