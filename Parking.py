n = int(input())
for _ in range(n):
    store1 = int(input())
    slut1 = list(map(int, input().split()))
    print((max(slut1) - min(slut1)) * 2)
