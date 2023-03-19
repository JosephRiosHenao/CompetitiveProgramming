# https://codeforces.com/problemset/problem/118/A
print("".join(["" if letter.lower() in ['a','e','i','o','u','y'] else "."+letter.lower() for idx, letter in enumerate([text for text in input()])]))