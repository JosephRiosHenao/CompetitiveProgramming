# https://codeforces.com/problemset/problem/510/A
y, x = map(int, input().split())
first = False
for iy in range(1,y+1):
    if iy%2 != 0: string = "#"*x 
    elif first: string = "#"+str("."*x)[1:]; first = not first
    else: string = str("."*(x-1))+"#"; first = not first
    print(string)