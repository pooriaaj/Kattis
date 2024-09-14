x = input()
t = len(x) // 3
a, b, c = x[:t], x[t:2*t], x[2*t:]
print(a if a == b or a == c else b)
