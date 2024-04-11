# https://codeforces.com/problemset/problem/467/A
rooms = [[int(room) for room in input().split()] for _ in range(int(input()))]
print(sum([1 if room[1]-room[0] >= 2 else 0 for room in rooms]))