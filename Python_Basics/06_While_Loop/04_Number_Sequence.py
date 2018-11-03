import math
import sys

max_number = -sys.maxsize - 1
min_number = sys.maxsize

while True:
    number = input()
    if number == "END":
        break
    else:
        number = int(number)

    if number <= min_number:
        min_number = number
    if number >= max_number:
        max_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
