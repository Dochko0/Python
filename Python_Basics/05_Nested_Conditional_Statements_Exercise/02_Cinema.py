category = input()
row = int(input())
column = int(input())

if category == "Premiere":
    profit = row*column * 12
    print(f'{profit:.2f} leva')
elif category == "Normal":
    profit = row*column * 7.5
    print(f'{profit:.2f} leva')
elif category == "Discount":
    profit = row * column * 5
    print(f'{profit:.2f} leva')