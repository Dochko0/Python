money_for_vacation = float(input())
curr_money = float(input())
days = 0
all_days = 0

while True:
    action = input()
    transfer_money = float(input())
    all_days += 1
    if action == 'spend':
        days += 1
        if days == 5:
            print(f'You can\'t save the money.')
            print(days)
            break
        elif curr_money >= transfer_money:
            curr_money -= transfer_money
        elif curr_money < transfer_money:
            curr_money = 0
    elif action == 'save':
        curr_money += transfer_money

    if curr_money >= money_for_vacation:
        print(f'You saved the money for {all_days} days.')
        break

