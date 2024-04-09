# https://codeforces.com/problemset/problem/4/B
days, sumTime = map(int,input().split())
daysList = [[int(time) for time in input().split()] for _ in range(days)]
minHSum = 0
maxHSum = 0
daysHours = [day[0] for day in daysList]
for day in range(days):
    minHSum += daysList[day][0]
    maxHSum += daysList[day][1]
if minHSum<=sumTime and maxHSum>=sumTime:
    print("YES")
    while sum(daysHours)<sumTime:
        for iday in range(days-1,-1,-1):
            if daysHours[iday] < daysList[iday][1]: daysHours[iday] += 1
            if sum(daysHours) == sumTime: break
    print(str(daysHours).replace(',','')[1:-1])    
else:
    print("NO")
    