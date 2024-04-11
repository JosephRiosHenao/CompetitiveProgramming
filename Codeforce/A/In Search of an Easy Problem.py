# https://codeforces.com/problemset/problem/1030/A
_, list = input(), [s for s in input().split()]
print("HARD") if str("".join(list)).count("1") >= 1 else print("EASY")
