import sys

n = int(input())
first_pair = 0
second_pair = 0
max_pair = -sys.maxsize
min_pair = sys.maxsize
max_diff = 0
count = 1

for i in range(1, n + 1):
    first_pair = 0
    for j in range(1, 2 + 1):
        num = int(input())
        if count == 1 or count == 2:
            first_pair += num
    # for k in range(1, 2 + 1):
    #     num2 = int(input())
    #     if count == 1 or count == 2:
    #         second_pair += num2
    # i += 1
    if first_pair >= max_pair:
        max_pair = first_pair
    # if second_pair>=max_pair:
    #     max_pair=second_pair
    if first_pair <= min_pair:
        min_pair = first_pair
    # if second_pair<=min_pair:
    #     min_pair=second_pair

if max_pair == min_pair:
    print(f'Yes, value={max_pair}')
else:
    print(f'No, maxdiff={max_pair-min_pair}')
