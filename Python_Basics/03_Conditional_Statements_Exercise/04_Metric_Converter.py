number = float(input())
inner = input()
outer = input()
meter = 0
result = 0
if inner == 'mm':
    meter = number / 1000
elif inner == 'cm':
    meter = number / 100
elif inner == 'mi':
    meter = number / 0.000621371192
elif inner == 'in':
    meter = number / 39.3700787
elif inner == 'km':
    meter = number / 0.001
elif inner == 'ft':
    meter = number / 3.2808399
elif inner == 'yd':
    meter = number / 1.0936133
else:
    meter = number

if outer == 'mm':
    result = meter * 1000
elif outer == 'cm':
    result = meter * 100
elif outer == 'mi':
    result = meter * 0.000621371192
elif outer == 'in':
    result = meter * 39.3700787
elif outer == 'km':
    result = meter * 0.001
elif outer == 'ft':
    result = meter * 3.2808399
elif outer == 'yd':
    result = meter * 1.0936133
else:
    result = meter

print(result)
