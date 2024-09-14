n = int(input())
for _ in range(n):
    cases = list(map(int, input().split()))
    average = sum(cases[1:]) / cases[0]
    counter = sum(1 for x in cases[1:] if x > average)
    print(f'{(counter / cases[0] * 100):.3f}%')
