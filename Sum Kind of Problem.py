numberOfTests = int(input())
for _ in range(numberOfTests):
    dataSetNumber, limit = map(int, input().split())

    totalSum = sum(range(limit + 1))
    evenSum = sum(range(0, limit * 2 + 1, 2))
    oddSum = sum(range(1, limit * 2 + 1, 2))

    print(f"{dataSetNumber} {totalSum} {oddSum} {evenSum}")
