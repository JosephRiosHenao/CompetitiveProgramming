# https://codeforces.com/problemset/problem/282/A
x = 0
for _ in range(0, int(input())):
    statement=input()
    if "++" in statement:x+=1
    if "--" in statement:x-=1
print(x)