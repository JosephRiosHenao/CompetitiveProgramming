# https://codeforces.com/problemset/problem/59/A
s = input()
s_up = [True if ids.isupper() else False for ids in s].count(True)
s_low = len(s)-s_up
print(s.lower()) if s_low>=s_up else print(s.upper()) 