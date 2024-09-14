n = int(input())

reverse_binary = f'{n:b}'[::-1]
reverse_integer = int(reverse_binary, 2)
print(reverse_integer)
