diamond = 0
bronze = 2
bmines = 0
silver = 0
smines = 0
gold = 0
gmines = 0
dmines = 0
answer_bmines = 0
answer_smines = 0
answer_gsmines = 0
answer_dmines = 0
number = 0

print('Welcome in game! You need to amass amount of 8 diamonds to win')
print('Rules: At the beginning of turn you will be able to buy something for goods you have. '
      'Each mine will produce goods each turn. You can always buy one mine each type. Your starting good: 2 bronze')
print('When you are asked about anything, 1 always means yes, 2 always means no' )
print('Bronze mine cost 2 bronze, Silver mine cost 8 bronze, Gold mine cost 8 silver, diamond mine cost 8 gold')

while diamond < 8:
    bronze = bronze + bmines
    silver = silver + smines
    gold = gold + gmines
    diamond = diamond + dmines
    print(f' You have now:{bronze} bronze, {silver} silver, {gold} gold, {diamond} diamonds')
    print(f' {bmines} bronze mines, {smines} silver mines, {gmines} gold mines, {dmines} diamond mines')
    if bronze > 1:
        answer_bmines = int(input('Would you like to buy bronze mine for 2 bronze?'))
        if answer_bmines < 2:
                bronze = bronze - 2
                bmines = bmines + 1
    if bronze > 7:
        answer_smines = int(input('Would you like to buy silver mine for 8 bronze?'))
        if answer_smines < 2:
            bronze = bronze - 8
            smines = smines + 1
    if silver > 7:
        answer_gsmines = int(input('Would you like to buy gold mine for 8 silver?'))
        if answer_gsmines < 2:
            silver = silver - 8
            gmines = gmines + 1
    if gold > 7:
        answer_dmines = int(input('Would you like to buy diamond mine for 8 gold?'))
        if answer_dmines < 2:
            gold = gold - 8
            dmines = dmines + 1
    number = number + 1
    print(f'End of turn {number}')

print(f'You won in {number} turns')