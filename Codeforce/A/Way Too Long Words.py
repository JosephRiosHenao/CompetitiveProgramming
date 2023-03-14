# https://codeforces.com/problemset/problem/71/A
for times in range(0,int(input())):
    word:str = input()
    print(word) if (len(word)<=10) else print(f"{word[0]}{len(word)-2}{word[-1]}")