import sys

count_numbers = int(input())
min = sys.maxsize

for i in range(1, count_numbers + 1):
    num = int(input())
    if num <= min:
        min = num

print(min)
