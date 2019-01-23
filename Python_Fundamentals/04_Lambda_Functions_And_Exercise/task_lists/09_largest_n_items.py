num_list = list(map(int, input().split()))

num_list.sort()
num_list.reverse()

items = int(input())

print(' '.join(str(num_list[x]) for x in range (0, items)))