number_list = list(map(int, input().split()))

swap = True

while swap:
    swap = False
    for i in range (1, len(number_list)):
        check_left = number_list[i - 1]
        check_right = number_list[i]
        if check_left>check_right:
            num = number_list[i]
            number_list[i] = number_list[i-1]
            number_list[i-1] = num
            swap = True

print(' '.join(str(x) for x in number_list))