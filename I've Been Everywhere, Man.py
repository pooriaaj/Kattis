n = int(input())
for _ in range(n):
    x = {}
    m = int(input())
    for _ in range(m):
        x[input()] = 1
    print(len(x))
