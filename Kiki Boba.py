word = input()
counterB = word.count('b')
counterK = word.count('k')

if counterB > counterK:
    print("boba")
elif counterK > counterB:
    print("kiki")
elif counterB == 0 and counterK == 0:
    print("none")
else:
    print("boki")
