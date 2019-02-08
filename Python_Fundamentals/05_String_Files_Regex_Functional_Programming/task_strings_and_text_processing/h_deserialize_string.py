

pos_dict = {}

while True:
    line = input()
    if line == "end":
        break

    val, keys = line.split(':')
    keys = keys.split('/')
    for key in keys:
        if key not in pos_dict:
            pos_dict[int(key)] = val


for x in sorted(pos_dict):
    print(f'{pos_dict[x]}', end='')