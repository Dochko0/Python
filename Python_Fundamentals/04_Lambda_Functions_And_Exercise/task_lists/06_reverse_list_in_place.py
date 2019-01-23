number_list = list(map(int, input().split()))

number_list.reverse()

print(" ".join(str(x) for x in number_list))