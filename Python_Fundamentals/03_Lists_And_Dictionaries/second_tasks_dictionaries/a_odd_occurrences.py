line_list = input().split()

line_list = [x.lower() for x in line_list]
dict = {}

for i in range(0, len(line_list)):
    num = line_list.count(line_list[i])
    if num%2!=0:
        dict[line_list[i]] = 1

print(", ".join(dict.keys()))

