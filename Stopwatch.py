s = []
n = int(input())
for _ in range(n):
    x = int(input())
    s.append(x)

if n % 2 == 1:
    print('still running')
else:
    even_sum = 0
    odd_sum = 0
    for i in range(len(s)):
        if i % 2 == 0:
            even_sum += s[i]
        else:
            odd_sum += s[i]
    print(odd_sum - even_sum)
