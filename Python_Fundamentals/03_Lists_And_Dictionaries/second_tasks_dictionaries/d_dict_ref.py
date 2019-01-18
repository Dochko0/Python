dict = {}

while True:
    line_list = input().split(" = ")
    if line_list[0] == "end":
        break

    if line_list[1].isdigit():
        dict[line_list[0]] = int(line_list[1])
    else:
        if line_list[1] in dict:
            dict[line_list[0]] = dict[line_list[1]]

for key, value in dict.items():
    print(f'{key} === {value}')
