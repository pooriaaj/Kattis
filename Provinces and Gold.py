gold, silver, copper = map(int, input().split())
power = 3 * gold + 2 * silver + copper

if power >= 8:
    status = 'Province'
elif power >= 5:
    status = 'Duchy'
elif power >= 2:
    status = 'Estate'
else:
    status = ''
if power >= 6:
    card = 'Gold'
elif power >= 3:
    card = 'Silver'
else:
    card = 'Copper'
if status:
    print(f"{status} or {card}")
else:
    print(card)
