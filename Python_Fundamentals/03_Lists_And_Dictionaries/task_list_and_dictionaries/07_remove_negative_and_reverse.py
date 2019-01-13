num_list = list(map(int, input().split(" ")))
positive_list = []

for i in range(0, len(num_list)):
    if num_list[i] > 0:
        positive_list.append(num_list[i])

positive_list.reverse()
if len(positive_list)==0:
    print('empty')
else:
    print(" ".join(str(x) for x in positive_list))
