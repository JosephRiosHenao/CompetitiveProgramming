# https://codeforces.com/problemset/problem/469/A
levels = int(input())
little_X = [int(x) for x in input().split()][1::]
little_Y = [int(y) for y in input().split()][1::]
total_levels = list(little_X+little_Y)
total_levels.sort()
total_levels = list(set(total_levels))
for level in range(1,levels+1,1):
    try:
        if total_levels[level-1] == level: continue
        else: raise()
    except Exception as e:
        print("Oh, my keyboard!")
        exit()
print("I become the guy.")