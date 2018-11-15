word = list(input().lower())

sum = 0

for a in word:
    if a == 'a':
        sum += 1
    elif a == 'e':
        sum += 2
    elif a == 'i':
        sum += 3
    elif a == 'o':
        sum += 4
    elif a == 'u':
        sum += 5

print(sum)
