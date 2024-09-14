g, t, n = map(int, input().split())
items = list(map(int, input().split()))
result = int(0.9 * (g - t) - sum(items))
print(result)
