number_of_words = int(input())
is_odd = False
for _ in range(number_of_words):
    is_odd = not is_odd
    word = input()
    if is_odd:
        print(word)
