n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    profit = e - c
    if r < profit:
        print("advertise")
    elif r == profit:
        print("does not matter")
    else:
        print("do not advertise")
