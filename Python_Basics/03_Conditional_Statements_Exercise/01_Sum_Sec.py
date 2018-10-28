sec1 = int(input())
sec2 = int(input())
sec3 = int(input())

sum = sec1+sec2+sec3

min = int(sum/60)
seconds = sum - min*60


if seconds<10:
    print(str(min) + ":0" + str(seconds))
else: print(str(min) + ":" + str(seconds))