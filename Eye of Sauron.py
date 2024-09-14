n = input()
x = n.split('()')
print('correct' if len(x[0]) == len(x[1]) else 'fix')
