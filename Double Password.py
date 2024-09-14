pass1 = input()
pass2 = input()
number_of_combinations = 1
for i, j in zip(pass1, pass2):
    if i != j:
        number_of_combinations *= 2
print(number_of_combinations)
