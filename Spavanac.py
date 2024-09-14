H, M = map(int, input().split())
if M < 45:
    minutes = M + 15
    hours = H - 1
    if hours < 0:
        hours = 23
else:
    minutes = M - 45
    hours = H

print(hours, minutes)
