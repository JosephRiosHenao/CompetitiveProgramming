from collections import Counter
input()
shoe_size = Counter([int(i.strip('"')) for i in input().split(' ')])
spend = 0
for _ in range(int(input())):
    size, value = map(int, input().split())
    if shoe_size[size] != 0:
        shoe_size[size] -= 1
        spend += value
print(spend)
