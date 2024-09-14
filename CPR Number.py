data = input()
ciphers = map(int, data[:6] + data[7:])
coefficients = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
result = sum(i * j for i, j in zip(ciphers, coefficients))

print(1 if result % 11 == 0 else 0)
