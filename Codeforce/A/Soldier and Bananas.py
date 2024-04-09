# https://codeforces.com/problemset/problem/546/A
k,n,w = list(map(int, input().split()))
print(max(0,(sum([i*k for i in range(1,w+1)])-n)))
