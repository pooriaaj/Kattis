length, horizental, vertical = map(int, input().split())
thickness = 4
maxhorizental = max(horizental, length - horizental)
maxvertical = max(vertical, length - vertical)
max_volume = maxhorizental * maxvertical * thickness
print(max_volume)
