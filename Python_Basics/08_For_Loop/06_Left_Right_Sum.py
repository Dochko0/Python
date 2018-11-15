count_num = int(input())
left = 0
right = 0

for i in range(1, count_num * 2 + 1):
    curr_num = int(input())
    if i <= count_num:
        left += curr_num
    else:
        right += curr_num

if left == right:
    print(f'Yes, sum = {left}')
elif left > right:
    print(f'No, diff = {left-right}')
else:
    print(f'No, diff = {right-left}')
