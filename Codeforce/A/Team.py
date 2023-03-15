# https://codeforces.com/problemset/problem/231/A
problems_solve = 0
for problems in range(0, int(input())):
    if (input().count("1")>=2): problems_solve += 1
print(problems_solve)