n = int(input())
for _ in range(n):
    phrase = input()
    if "Simon says" in phrase:
        print(phrase[11:])
