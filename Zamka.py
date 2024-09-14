lower_digit = int(input())
higher_digit = int(input())
expected_sum = int(input())
chosen = []

for i in range(lower_digit, higher_digit + 1):
    if sum(int(digit) for digit in str(i)) == expected_sum:
        chosen.append(i)

print(chosen[0])
print(chosen[-1])
