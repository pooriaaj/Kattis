n = input().upper()
vowels = {'A', 'E', 'I', 'O', 'U'}
count = sum(1 for char in n if char in vowels)
print(count)
