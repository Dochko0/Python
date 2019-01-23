names_dict = {}

while True:
    line_input = input().split(' -> ')
    if line_input[0] == 'end':
        break

    if line_input[0] not in names_dict:
        names_dict[line_input[0]] = []

    if line_input[1] in names_dict:
        names_dict[line_input[0]].extend(names_dict[line_input[1]])
    else:
        try:
            numbers = list(map(int, line_input[1].split(', ')))
            names_dict[line_input[0]].extend(numbers)
        except ValueError:
            if len(names_dict[line_input[0]]) == 0:
                del names_dict[line_input[0]]

for x in names_dict:
    print(f'{x} === '+', '.join(str(y) for y in names_dict[x]))





