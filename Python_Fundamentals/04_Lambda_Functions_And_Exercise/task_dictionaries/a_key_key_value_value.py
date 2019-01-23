key = input().strip()
value = input().strip()
count = int(input())

result = ''
for entry in range(count):
    keys, values = input().split(' => ')
    if key in keys:
        result += f'{keys}:\n'
        if value in values:
            all_values = '\n'.join([f'-{v}' for v in values.split(';') if value in v])
            result += f'{all_values}\n'

print(result)