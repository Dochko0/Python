line_list = input().split("|")
number_list = []

for i in range(len(line_list) - 1, -1, -1):
    # some_list = line_list[i].split()
    number_list += line_list[i].split()


print(" ".join(str(x) for x in number_list))
