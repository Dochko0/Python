count_num = int(input())
odd = 0
even = 0

for i in range(1, count_num + 1):
    curr_num = int(input())
    if i % 2 == 0:
        odd += curr_num
    else:
        even += curr_num

if odd == even:
    print(f'Yes, sum = {odd}')
elif odd > even:
    print(f'No, diff = {odd-even}')
else:
    print(f'No, diff = {even-odd}')
