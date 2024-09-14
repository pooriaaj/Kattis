wind_speed = int(input())
roads = int(input())

for _ in range(roads):
    road_condition = input().split()
    road_name = road_condition[0]
    road_wind = int(road_condition[1])
    difference = wind_speed - road_wind
    
    if difference > 0:
        print(road_name, 'lokud')
    else:
        print(road_name, 'opin')
