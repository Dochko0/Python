numbers_list = list(map(int, input().split(" ")))

def multiply (num, multi_num):
    num = num*multi_num
    return num


multi_num = int(input())

for i in range (0, len(numbers_list)):
    numbers_list[i] = multiply(numbers_list[i], multi_num)

print(" ".join(list(map(str,numbers_list))))