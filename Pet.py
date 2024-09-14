s = []
for _ in range(5):
    a, b, c, d = map(int, input().split())
    s.append(a + b + c + d)

max_sum = max(s)
for i in range(5):
    if s[i] == max_sum:
        index = i
        break

print(index + 1, max_sum)
