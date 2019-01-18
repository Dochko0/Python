dict = {}

while True:
    line_list = input().split(" : ")
    if line_list[0] == "Over":
        break
    if line_list[0].isdigit():
        dict[line_list[1]] = line_list[0]
    else:
        dict[line_list[0]] = line_list[1]

for key,value in sorted(dict.items()):
    print(f'{key} -> {value}')