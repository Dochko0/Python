width = float(input())
length = float(input())
count_pieces = width * length

while True:
    command = input()
    if command == 'STOP':
        break
    else:
        command = float(command)
        count_pieces -= command
        if count_pieces < 0:
            print(f'No more cake left! You need {count_pieces*-1:.0f} pieces more.')
            break

if count_pieces >= 0:
    print(f'{count_pieces:.0f} pieces are left.')
