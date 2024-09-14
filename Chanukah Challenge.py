n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    s = (y * (y + 3)) // 2
    print(x, s)
