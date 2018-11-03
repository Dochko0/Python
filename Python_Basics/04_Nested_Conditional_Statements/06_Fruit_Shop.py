fruit = input()
day_of_week = input()
quantity = float(input())

if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        total_price = quantity * 2.7
        print(total_price)
    elif fruit == "apple":
        total_price = quantity * 1.25
        print(total_price)
    elif fruit == "orange":
        total_price = quantity * 0.9
        print(total_price)
    elif fruit == "grapefruit":
        total_price = quantity * 1.6
        print(total_price)
    elif fruit == "kiwi":
        total_price = quantity * 3
        print(total_price)
    elif fruit == "pineapple":
        total_price = quantity * 5.6
        print(total_price)
    elif fruit == "grapes":
        total_price = quantity * 4.2
        print(total_price)
    else:
        print("error")
elif day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week=="Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        total_price = quantity * 2.5
        print(total_price)
    elif fruit == "apple":
        total_price = quantity * 1.2
        print(total_price)
    elif fruit == "orange":
        total_price = quantity * 0.85
        print(total_price)
    elif fruit == "grapefruit":
        total_price = quantity * 1.45
        print(total_price)
    elif fruit == "kiwi":
        total_price = quantity * 2.7
        print(total_price)
    elif fruit == "pineapple":
        total_price = quantity * 5.5
        print(total_price)
    elif fruit == "grapes":
        total_price = quantity * 3.85
        print(total_price)
    else:
        print("error")
else:
    print("error")