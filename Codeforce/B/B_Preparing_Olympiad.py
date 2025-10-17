# https://codeforces.com/contest/550/problem/B
def solve():
    n, l, r, x = map(int, input().split())
    diff = list(map(int, input().split()))
 
    ans = 0
 
    for mask in range(1, 1 << n):
        subset = [diff[i] for i in range(n) if mask & (1 << i)]
 
        if len(subset) < 2:
            continue
 
        total = sum(subset)
        if not (l <= total <= r):
            continue
 
        if max(subset) - min(subset) < x:
            continue
 
        ans += 1
 
    print(ans)
 
 
if __name__ == '__main__':
    solve()