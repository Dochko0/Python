product = input()
town = input()
quantity = float(input())

if product == "coffee":
    if town == "Sofia":
        price = quantity * 0.5
        print(price)
    elif town == "Plovdiv":
        price = quantity * 0.4
        print(price)
    elif town == "Varna":
        price = quantity * 0.45
        print(price)
elif product == "water":
    if town == "Sofia":
        price = quantity * 0.8
        print(price)
    elif town == "Plovdiv":
        price = quantity * 0.7
        print(price)
    elif town == "Varna":
        price = quantity * 0.7
        print(price)
elif product == "beer":
    if town == "Sofia":
        price = quantity * 1.2
        print(price)
    elif town == "Plovdiv":
        price = quantity * 1.15
        print(price)
    elif town == "Varna":
        price = quantity * 1.1
        print(price)
elif product == "sweets":
    if town == "Sofia":
        price = quantity * 1.45
        print(price)
    elif town == "Plovdiv":
        price = quantity * 1.3
        print(price)
    elif town == "Varna":
        price = quantity * 1.35
        print(price)
elif product == "peanuts":
    if town == "Sofia":
        price = quantity * 1.6
        print(price)
    elif town == "Plovdiv":
        price = quantity * 1.5
        print(price)
    elif town == "Varna":
        price = quantity * 1.55
        print(price)