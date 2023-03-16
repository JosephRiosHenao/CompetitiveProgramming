# https://codeforces.com/problemset/problem/1/A
from math import floor
n,m,a = input().split(' ')
n, m, a = int(n), int(m), int(a)
m = floor(m/a + (m%a!=0))
n = floor(n/a + (n%a!=0))
print(m*n)