text = input()
text = list(text)

while True:
    command = input()
    if command == 'end':
        break

    command = command.split()

    if command[0] == 'Left':
        for r in range(0, int(command[1])):
            first_index = text[0]
            for i in range(1, len(text)):
                text[i - 1] = text[i]
            text[len(text) - 1] = first_index
    if command[0] == 'Right':
        for r in range(0, int(command[1])):
            first_index = text[len(text) - 1]
            for i in range(len(text) - 2, -1, -1):
                text[i + 1] = text[i]
            text[0] = first_index
    if command[0]== 'Delete':
        del text[int(command[1]):int(command[2])+1]
    if command[0] == 'Insert':
        a = command[1]
        b = command[2]
        text.insert(int(command[1]), command[2])




print(''.join(x for x in text))
