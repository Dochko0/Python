budget = float(input())
begin = budget
balloons_count = 0
ribbon_size = 0
flowers_count = 0
candles_count = 0

while True:
    if budget<=0:
        break
    stock = input()
    if stock == 'stop':
        break

    count_stock = float(input())

    if stock == 'balloons':
        balloons_count+=count_stock
        budget-= count_stock*0.1
    elif stock == 'flowers':
        flowers_count+=count_stock
        budget-= count_stock*1.5
    elif stock == 'candles':
        candles_count+=count_stock
        budget-=count_stock*0.5
    elif stock == 'ribbon':
        ribbon_size+=count_stock
        budget-= count_stock * 2

if budget>0:
    print(f'Spend money: {begin-budget:.2f}')
    print(f'Money left: {budget:.2f}')
else:
    print('All money is spent!')

print(f'Purchased decoration is {balloons_count:.0f} balloons, {ribbon_size:.0f} m ribbon, {flowers_count:.0f} flowers and {candles_count:.0f} candles.')