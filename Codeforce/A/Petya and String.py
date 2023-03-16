# https://codeforces.com/problemset/problem/112/A
str_input = [input() for _ in range(2)]
print(0 if str_input[0].upper() == str_input[1].upper() else 1 if str_input[0].upper()>str_input[1].upper() else -1)