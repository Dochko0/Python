import sys

count_numbers = int(input())
max = -sys.maxsize

for i in range(1, count_numbers+1):
    num = int(input())
    if num>=max:
        max=num

print(max)