match = [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[', ']','?']
words = input()
for s in match:
    words = words.replace(s, " ")

words = list(words.split())

lower_list = []
upper_list = []
mix_list = []

for n in words:
    if n.lower() == n and not n.isdigit() and n.isalpha():
        lower_list.append(n)
    elif n.upper() == n and not n.isdigit() and n.isalpha():
        upper_list.append(n)
    else:
        mix_list.append(n)

separator = ', '

print(f'Lower-case: {separator.join(lower_list)}')
print(f'Mixed-case: {separator.join(mix_list)}')
print(f'Upper-case: {separator.join(upper_list)}')