mililiters = int(input())
count = 0
while mililiters > 0:
    word = input()
    if word == "Easy":
        mililiters -= 50
    elif word == 'Medium':
        mililiters -= 100
    elif word == 'Hard':
        mililiters -= 200
    count += 1
if mililiters < 0:
    print(f'{mililiters*-1}ml has been spilled.')
else:
    print(f'The dispenser has been tapped {count} times.')
