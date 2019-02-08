text = input()
letters_dict = {}

for i in range (0, len(text)):
    if text[i] not in letters_dict:
        letters_dict[text[i]] = [i]
    else:
        letters_dict[text[i]].append(i)

for x in letters_dict:
    print(f'{x}:' + '/'.join(str(z) for z in letters_dict[x]))