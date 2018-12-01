partida = int(input())
counter = 0
flour = False
sugar = False
eggs = False

while partida > 0:
    product = input()
    if product == 'flour':
        flour = True
    elif product == 'sugar':
        sugar = True
    elif product == 'eggs':
        eggs = True

    if product == 'Bake!' and flour == True and sugar == True and eggs == True:
        counter += 1
        partida -= 1
        flour = False
        sugar = False
        eggs = False
        print(f'Baking batch number {counter}...')
    elif product == 'Bake!' and (flour == False or sugar == False or eggs == False):
        print('The batter should contain flour, eggs and sugar!')
