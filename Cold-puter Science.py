n = int(input())
s = 0
for _ in range(n):
    row = map(int, input().split())
    s += sum(1 for i in row if i < 0)
print(s)
