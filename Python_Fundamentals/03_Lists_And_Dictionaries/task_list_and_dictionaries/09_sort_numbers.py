line_list = list(map(int, input().split()))

line_list.sort()

print(" <= ".join(str(x) for x in line_list))