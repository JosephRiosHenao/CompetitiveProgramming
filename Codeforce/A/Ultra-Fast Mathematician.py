# https://codeforces.com/problemset/problem/61/A
n1, n2 = input().strip(), input().strip()
print("".join(["0" if i==n2[idx] else "1" if i=="1" or n2[idx]=="1" else "0" for idx, i in enumerate(n1)]))