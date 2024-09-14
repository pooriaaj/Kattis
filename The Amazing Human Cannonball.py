import math

n = int(input())
for _ in range(n):
    velocity, angle, x_position, lower_height, upper_height = map(float, input().split())
    gravity = 9.81
    radians = math.radians(angle)
    t_x0 = x_position / (velocity * math.cos(radians))
    jump = velocity * t_x0 * math.sin(radians)
    failure = 0.5 * gravity * (t_x0 ** 2)
    y_t = jump - failure
    if lower_height + 1 <= y_t <= upper_height - 1:
        print('safe')
    else:
        print('not safe')
