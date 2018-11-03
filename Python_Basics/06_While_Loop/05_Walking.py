steps = 0

while steps<10000:
    curr = input()
    if curr=="Going home":
        last_steps = int(input())
        steps+=last_steps
        break
    else:
        curr = int(curr)

    steps += curr

if steps<10000:
    diff = 10000-steps
    print(f'{diff} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
