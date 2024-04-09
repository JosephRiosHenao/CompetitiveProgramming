# https://codeforces.com/problemset/problem/339/B
max_path = int(input().split()[0])
todo_list = list(map(int,input().split()))
steps, after, num = 0, 0, 0
for todo in todo_list:
    if todo < num: steps += max_path+todo-num 
    else: steps += todo-num
    num = todo
print(steps-1)