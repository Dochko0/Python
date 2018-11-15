import sys
import math

numbers = int(input())


max = -sys.maxsize
sum = 0

for i in range(1, numbers + 1):
    num = int(input())
    if i == 1 and max <= num:
        # sum = 0
        max = num
    elif max <= num:
        sum += max
        max = num
    else:
        sum += num

if sum == max:
    print(f"Yes\nSum = {sum:.0f}")
else:
    print(f'No\nDiff = {math.fabs(sum-max):.0f}')
