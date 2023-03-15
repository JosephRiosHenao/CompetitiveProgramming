# https://codeforces.com/problemset/problem/1/A
square = int(input())*int(input()) 
slab = int(input())**2
result = square-(slab*int(square/slab))
print(result)
