age = int(input())
price = float(input())
toy_price = float(input())
money = 0
toys = 0
evaluation = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        evaluation += 10
        money = (money + evaluation - 1)

    else:
        toys += 1

money += toys * toy_price

if money >= price:
    print(f'Yes! {money-price:.2f}')
else:
    print(f'No! {price-money:.2f}')
