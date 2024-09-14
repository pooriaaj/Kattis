x = 0
input()  # Discard the first input
a = input().split()
for i in a:
    if i[0] == '-':
        x -= int(i)
print(x)
