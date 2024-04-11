# https://codeforces.com/problemset/problem/734/A
_ = input(); s = input(); A = s.count('A'); D = s.count('D')
print("Friendship") if A==D else print("Anton") if A>D else print("Danik")