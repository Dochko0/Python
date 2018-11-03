month = input()
overnight = int(input())
apartment = 0
studio = 0

if month == 'May' or month == 'October':
    apartment = overnight * 65
    studio = overnight * 50
    if 7 < overnight <= 14:
        studio = studio * 0.95
    elif overnight > 14:
        apartment = apartment * 0.9
        studio = studio * 0.7

elif month == 'June' or month == 'September':
    apartment = overnight * 68.7
    studio = overnight * 75.2
    if overnight > 14:
        apartment = apartment * 0.9
        studio = studio * 0.8

elif month == 'July' or month == 'August':
    apartment = overnight * 77
    studio = overnight * 76
    if overnight > 14:
        apartment = apartment * 0.9

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
