n = int(input())
for _ in range(n):
    sets, base, integer = map(int, input().split())
    result = 0
    while integer > 0:
        cipher = integer % base
        integer //= base
        result += cipher ** 2
    print(f"{sets} {result}")
