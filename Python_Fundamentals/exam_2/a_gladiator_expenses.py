loss_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
isSword = True
isHelmet = True
isShield=True

for i in range(1, loss_count + 1):
    if i % 2 == 0:
        broken_helmet += 1
        isHelmet = False
    if i % 3 == 0:
        broken_sword += 1
        isSword = False
    if isHelmet == False and isSword == False:
        broken_shield += 1
        isShield=False
    if broken_shield > 0 and broken_shield % 2 == 0 and isShield==False:
        broken_armor += 1
    isSword = True
    isHelmet = True
    isShield = True

total_price = broken_helmet * helmet_price + broken_sword * sword_price + broken_shield \
              * shield_price + broken_armor * armor_price

print(f'Gladiator expenses: {total_price:.2f} aureus')
