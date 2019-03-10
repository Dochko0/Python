while True:
    incoming = input()
    if incoming == 'stop playing':
        break

    line_input = list(map(int, incoming.split()))

    if len(line_input) == len(set(line_input)):
        for x in range(0, len(line_input)):
            if line_input[x] % 2 == 0:
                line_input[x] += 2

        sort_list = sorted(line_input)

        print('Unique list: ' + f','.join(str(x) for x in sort_list))
        print('Output: ' + f'{sum(sort_list)/len(sort_list):.2f}')

    else:
        for x in range(0, len(line_input)):
            if line_input[x] % 2 != 0:
                line_input[x] += 3

        sort_list = sorted(line_input)

        print('Non-unique list: ' + f':'.join(str(x) for x in sort_list))
        print('Output: ' + f'{sum(sort_list)/len(sort_list):.2f}')
