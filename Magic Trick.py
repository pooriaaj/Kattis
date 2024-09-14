n = input()
for i in n:
    if n.count(i) > 1:
        print(0)
        break
else:
    print(1)
