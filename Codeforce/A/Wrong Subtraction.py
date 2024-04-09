# https://codeforces.com/problemset/problem/977/A
n, mn = [int(n) for n in input().split()]
def define_n(value): n = value; print(n)
[define_n(n/10) if str(n)[-1]=='0' else define_n(int( str(n)[:-1]+str(int(str(n)[-1])-1) )) for _ in range(mn)]
print(n)