line, num = ['1'] * int(input()), 2
for i in map(int, input().split()):
    line[1 + i], num = str(num), num + 1
print(' '.join(line))
