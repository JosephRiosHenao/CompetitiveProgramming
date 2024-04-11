# https://codeforces.com/problemset/problem/133/A
s = input()
print("YES") if s.count("H") >= 1 or s.count("Q") >= 1 or \
s.count("9") >= 1 else print("NO")