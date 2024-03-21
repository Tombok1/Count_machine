amount = int(input('How much parts you want to buy?'))
parts = range(0, amount)
costs = []
main = int(1400)
diff1 = 0
diff = 0
cost_temp = 0
cost_temp1 = 0
def cost_collector(parts):
    for part in parts:
        part = int(input('How much this part costs?'))
        costs.append(part)

def cost_counter():
    cost_collector(parts)
    diff = main - costs[0]
    costs.pop(0)
    print(diff)

    for cost in costs:
        if diff < main - cost:
            if cost_temp < cost:
                cost_temp = cost
                diff1 = diff - cost_temp
    print(diff1)

    for cost in costs:
            if cost_temp > cost:
                cost_temp1 = cost
                diff1 = diff1 - cost_temp1
    print(diff1)
cost_counter()
