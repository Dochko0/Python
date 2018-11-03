num_deposits = int(input())
all_money = 0.0

while num_deposits > 0:
    incoming = float(input())
    if incoming<0:
        print('Invalid operation!')
        break
    print(f'Increase: {incoming:.2f}')
    all_money += incoming
    num_deposits -= 1

print(f'Total: {all_money:.2f}')
