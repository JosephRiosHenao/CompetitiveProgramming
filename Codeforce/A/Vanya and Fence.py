# https://codeforces.com/problemset/problem/677/A
fance_h = int(input().split()[1]); n_h = list(map(int, input().split())); result = 0
for h in n_h: result += 1 if h<=fance_h else 2
print(result)