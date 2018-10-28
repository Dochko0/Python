price_of_trip = float(input())
puzzles = float(input())
talking_doll = float(input())
bears = float(input())
minions = float(input())
truck = float(input())

puzzle_price = 2.6
talking_doll_price = 3
bear_price = 4.1
minions_price = 8.2
truck_price = 2

first_price = puzzles*puzzle_price+talking_doll*talking_doll_price + \
              bears*bear_price + minions*minions_price + truck*truck_price

count_toys = puzzles+talking_doll+bears+minions+truck

if count_toys>=50:
    first_price = first_price*0.75

first_price = first_price*0.9

final_result = first_price - price_of_trip

if final_result>=0:
    print('Yes! ' + str(format(final_result, '.2f')) + ' lv left.')
else: print('Not enough money! '+ str(format(final_result*-1,'.2f')) + ' lv needed.')


