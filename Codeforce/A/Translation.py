# https://codeforces.com/problemset/problem/41/A
s1 = input()
s2 = "".join([s1[i] for i in range(len(s1)-1,-1,-1)])
print("YES") if input()==s2 else print("NO")