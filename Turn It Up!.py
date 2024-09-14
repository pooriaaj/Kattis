start_point = 7
n = int(input())
for _ in range(n):
    command = input()
    if 'op' in command and start_point < 10:
        start_point += 1
    elif 'ned' in command and start_point > 0:
        start_point -= 1

print(start_point)
