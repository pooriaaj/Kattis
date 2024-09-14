def details():
    phrase1 = input()
    phrase2 = input()
    comparison = ''.join('.' if j == k else '*' for j, k in zip(phrase1, phrase2))
    
    print(phrase1)
    print(phrase2)
    print(comparison)
    print()

n = int(input())
for _ in range(n):
    details()
