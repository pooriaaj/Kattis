while True:
    n = int(input())
    if n == -1:
        break
    previousTotalTimeElapsed = 0
    totalDistance = 0
    for _ in range(n):
        speedPerhour, totalElapsedTime = map(int, input().split())
        TotalTimeSpared = totalElapsedTime - previousTotalTimeElapsed
        previousTotalTimeElapsed = totalElapsedTime
        totalDistance += TotalTimeSpared * speedPerhour
    print(f'{totalDistance} miles')
