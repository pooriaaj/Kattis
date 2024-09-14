n = input()
s = n[0]  # Initialize with the first character
for i in range(1, len(n)):
    if n[i] != n[i - 1]:
        s += n[i]
print(s)
