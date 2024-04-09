# https://codeforces.com/problemset/problem/791/A
n1, n2, cont = [int(n) for n in input().split()] + [0]
while n1 <= n2: n1 *= 3; n2 *= 2; cont += 1
print(cont)