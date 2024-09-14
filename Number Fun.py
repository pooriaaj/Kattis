n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if any(
        a + b == c or b + a == c or
        a - b == c or b - a == c or
        a / b == c or b / a == c or
        a * b == c or b * a == c
    ):
        print('possible')
    else:
        print('impossible')
