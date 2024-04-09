# https://codeforces.com/gym/104252/problem/D


data = [int(strg) for strg in input().split(" ")]

home = data[1]
work = data[2]

days = [[True if day=="Y" else False for day in input().split(" ")] for _ in range(data[0]) ]


for idx_day, day in enumerate(days):
    print(f"{day} - {home} - {work}")
    
    home_travel = "N"
    work_travel = "N"

    if day[0]:
        home_travel = "Y"
        home-=1
        work+=1
    if day[1]:
        work_travel = "Y"
        work-=1
        home+=1
        

    # SI NO TIENE UMBRELLAS DISPONIBLES
    if not work:
        home_travel = "Y"
        work+=1
        home-=1
    elif not home: 
        work_travel = "Y" 
        home+=1
        work-=1

    print(f"{home_travel} {work_travel}")