town = input().lower()
sell_count = float(input())

if 0<=sell_count<=500:
    if town == "sofia":
        comission = sell_count*0.05
        print(f'{comission:.2f}')
    elif town=="varna":
        comission = sell_count * 0.045
        print(f'{comission:.2f}')
    elif town == "plovdiv":
        comission = sell_count * 0.055
        print(f'{comission:.2f}')
    else:
        print('error')
elif 500<sell_count<=1000:
    if town == "sofia":
        comission = sell_count*0.07
        print(f'{comission:.2f}')
    elif town=="varna":
        comission = sell_count * 0.075
        print(f'{comission:.2f}')
    elif town == "plovdiv":
        comission = sell_count * 0.08
        print(f'{comission:.2f}')
    else:
        print('error')
elif 1000<sell_count<=10000:
    if town == "sofia":
        comission = sell_count*0.08
        print(f'{comission:.2f}')
    elif town=="varna":
        comission = sell_count * 0.10
        print(f'{comission:.2f}')
    elif town == "plovdiv":
        comission = sell_count * 0.12
        print(f'{comission:.2f}')
    else:
        print('error')
elif 10000 < sell_count:
    if town == "sofia":
        comission = sell_count*0.12
        print(f'{comission:.2f}')
    elif town=="varna":
        comission = sell_count * 0.13
        print(f'{comission:.2f}')
    elif town == "plovdiv":
        comission = sell_count * 0.145
        print(f'{comission:.2f}')
    else:
        print('error')
else:
    print('error')