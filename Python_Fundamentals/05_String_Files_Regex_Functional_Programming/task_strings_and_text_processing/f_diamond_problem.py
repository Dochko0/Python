import re

line_input = input().lower()
pattern = r'<\w+>'
result = re.findall(pattern, line_input)
sum = 0
is_found = False

for x in result:
    is_found = True
    for y in x:
        if y.isdigit():
            sum += int(y)
    if sum > 0:
        print(f'Found {sum} carat diamond')
    sum = 0

if not is_found:
    print('Better luck next time')
