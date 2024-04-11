# https://codeforces.com/problemset/problem/977/A
n, mn = [int(n) for n in input().split()]
for _ in range(mn):
    n = int(n/10) if str(n)[-1]=='0' else n-1
print(n)
