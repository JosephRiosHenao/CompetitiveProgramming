# https://codeforces.com/problemset/problem/136/A
_, presents = input(), {int(s):ids+1 for ids, s in enumerate(input().split())}
print(str(dict(sorted(presents.items())).values())[13:-2].replace(',',''))