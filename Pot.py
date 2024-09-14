total = 0
for _ in range(int(input())):
    pots = input()
    pot = int(pots[:-1])
    power = int(pots[-1])
    total += pot ** power 

print(total)
