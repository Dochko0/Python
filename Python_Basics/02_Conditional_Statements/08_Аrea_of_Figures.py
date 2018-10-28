import math

figure = input()

if figure== 'square':
    side = float(input())
    result = side*side
    print(result)
elif figure=='rectangle':
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
    print(result)
elif figure == 'circle':
    radius = float(input())
    result = radius * radius * math.pi
    print(result)
elif figure== 'triangle':
    side = float(input())
    high = float(input())
    result = side *high /2
    print(result)