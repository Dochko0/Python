shop_dict = {}

while True:
    line = input().split()
    if line[0] + " " + line[1] == 'shopping time':
        break
    if line[1] in shop_dict and line[0] == 'stock':
        shop_dict[line[1]] += int(line[2])
    else:
        shop_dict[line[1]] = int(line[2])

while True:
    line_buy = input().split()
    if line_buy[0] + " " + line_buy[1] == 'exam time':
        break
    if line_buy[1] in shop_dict and line_buy[0] == 'buy':
        if shop_dict[line_buy[1]] == 0:
            print(f"{line_buy[1]} out of stock")
        elif shop_dict[line_buy[1]] <= int(line_buy[2]):
            shop_dict[line_buy[1]] = 0
        else:
            shop_dict[line_buy[1]] -= int(line_buy[2])
    else:
        print(f"{line_buy[1]} doesn't exist")

for key, value in shop_dict.items():
    if value > 0:
        print(f'{key} -> {value}')
