text = input()
case = input()
sum = 0

if case == 'UPPERCASE':
    for letter in text:
        if letter.isalpha() and letter == letter.upper():
            sum += ord(letter)
else:
    for letter in text:
        if letter.isalpha() and letter == letter.lower():
            sum += ord(letter)

print(f'The total sum is: {sum}')