# https://codeforces.com/problemset/problem/281/A
print("".join([letter.upper() if idx==0 else letter for idx, letter in enumerate([text for text in input()])]))