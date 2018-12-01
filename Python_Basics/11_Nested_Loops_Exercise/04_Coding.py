num = input()[::-1]
# num = num[::-1]

for i in num:
    if int(i)==0:
        print("ZERO")
    else:
        symbol = chr(int(i) + 33)
        print(symbol*int(i))
