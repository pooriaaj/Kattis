import math

n = int(input())
for _ in range(n):
    encoded_message = input()
    row_length = int(math.sqrt(len(encoded_message)))
    rows = [encoded_message[i*row_length:(i+1)*row_length][::-1] for i in range(row_length)]
    message = ''.join(''.join(row) for row in zip(*rows))
    print(message)
