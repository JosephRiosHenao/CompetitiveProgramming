# https://codeforces.com/problemset/problem/110/A
s=input(); len_s = s.count('7')+s.count('4')
print("YES") if len_s in [4,7] else print("NO")