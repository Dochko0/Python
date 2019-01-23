line_list = list(map(float, input().split()))

counter = {}

for number in line_list:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

for x in sorted(counter):
    print(f'{int(x)} -> {counter[x]}')
