numbers_list = list(map(int, input().split(" ")))

for i in range(1, len(numbers_list), 2):
    num = numbers_list[i]

    if num % 2 != 0:
        print(f'Index {i} -> {num}')
