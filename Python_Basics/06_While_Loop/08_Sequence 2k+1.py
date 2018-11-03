target = int(input())
number = 1
print(number)
while True:
    if number>=target:
        break
    number = number * 2 + 1
    if number>target:
        break
    print(number)

