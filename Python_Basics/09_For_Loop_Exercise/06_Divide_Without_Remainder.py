n = int(input())
divide2 = 0
divide3 = 0
divide4 = 0

for i in range(1, n + 1):
    num = int(input())
    if num % 2 == 0:
        divide2 += 1
    if num % 3 == 0:
        divide3 += 1
    if num % 4 == 0:
        divide4 += 1

percent_divide2 = (divide2 / n) * 100
percent_divide3 = (divide3 / n) * 100
percent_divide4 = (divide4 / n) * 100

print(f'{percent_divide2:.2f}%')
print(f'{percent_divide3:.2f}%')
print(f'{percent_divide4:.2f}%')
