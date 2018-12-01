food_money_per_day = float(input())
souvenirs_money_per_day = float(input())
hotel_money_per_day = float(input())

money_for_benzin = 29.4 * 1.85
money_for_food_and_souvenirs = food_money_per_day * 3 + souvenirs_money_per_day * 3
money_for_hotel = hotel_money_per_day * 0.9 + hotel_money_per_day * 0.85 + hotel_money_per_day * 0.8
all_money = money_for_benzin+money_for_food_and_souvenirs+money_for_hotel

print(f'Money needed: {all_money:.2f}')
