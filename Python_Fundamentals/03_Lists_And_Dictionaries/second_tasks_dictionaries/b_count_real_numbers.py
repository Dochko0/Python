num_list = list(map(float, input().split()))
dict = {}

for x in num_list:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

# sorted(dict)

for key in sorted(dict):
    print('%s -> %s times' % (key, dict[key]))
