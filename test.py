amount = int(input('How much parts you want to buy?'))
parts_number = range(0, amount)
costs = []
main = int(1400)
diff =[]
parts =[]
combo =[]
for i in parts_number:
    part = {
        'cost':  int(input('How muc this part costs?')),
        'name': str(input('What is product name?'))
    }
    parts.append(part)

for part in parts:
    for second_part in parts:
        print(part, second_part)
        onecombo = []
        onecombo.append(part)
        onecombo.append(second_part)
        combo.append(onecombo)
print(combo)
def combinator(parts, combo):
    for c in combo:
        for part in parts:
            c.append(part)

combinator(parts, combo)
print(combo)