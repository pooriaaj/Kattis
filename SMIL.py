n = list(input())
SingularSymbols = ''
DoubleSymbols = ''
for i, j in enumerate(n):
    OneSymbols = DoubleSymbols + j
    TwoSymbols = SingularSymbols + DoubleSymbols + j
    if OneSymbols in [":)", ";)"]:
        print(i - 1)

    if TwoSymbols in [":-)", ";-)"]:
        print(i - 2)

    SingularSymbols = DoubleSymbols
    DoubleSymbols = j
