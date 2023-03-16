# https://codeforces.com/problemset/problem/158/A
res = 0
first= input().split(' ')
second = input().split(" ")
for a in second:
   if int(a) >= int(second[int(first[1])-1]) and int(a) != 0: res+=1
print(res)

