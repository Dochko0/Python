fruit = input()
size_set = input()
count_sets = float(input())
price_set = 0

if fruit == 'Watermelon':
    if size_set == 'small':
        price_set = count_sets * 56 * 2
    elif size_set == 'big':
        price_set = count_sets * 28.7 * 5
elif fruit == 'Mango':
    if size_set == 'small':
        price_set = count_sets * 36.66 * 2
    elif size_set == 'big':
        price_set = count_sets * 19.60 * 5
elif fruit == 'Pineapple':
    if size_set == 'small':
        price_set = count_sets * 42.1 * 2
    elif size_set == 'big':
        price_set = count_sets * 24.8 * 5
elif fruit == 'Raspberry':
    if size_set == 'small':
        price_set = count_sets * 20 * 2
    elif size_set == 'big':
        price_set = count_sets * 15.2 * 5

if 400 <= price_set <= 1000:
    price_set = price_set * 0.85
elif price_set > 1000:
    price_set = price_set * 0.5

print(f'{price_set:.2f} lv.')
