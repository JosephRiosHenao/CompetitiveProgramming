# https://codeforces.com/problemset/problem/705/A
print(" ".join(["I love that" if i%2==0 else "I hate that" for i in range(1,int(input())+1)])[:-4]+"it")