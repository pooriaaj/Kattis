import math

cards = input()
numberoftablets = 0
numberofcompass = 0
numberofgears = 0

for letter in cards:
    if letter == 'T':
        numberoftablets += 1
    elif letter == 'C':
        numberofcompass += 1
    elif letter == 'G':
        numberofgears += 1
    else:
        exit(f'{letter} is not supported')

numberofsets = min(numberoftablets, numberofcompass, numberofgears)
score = numberoftablets ** 2 + numberofcompass ** 2 + numberofgears ** 2 + 7 * numberofsets
print(score)
