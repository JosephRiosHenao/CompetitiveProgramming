# https://codeforces.com/problemset/problem/520/A
pangram = input()

[print("NO") if pangram.count(letter) > 1 else print(f"BIEN LETRA {letter}") for letter in pangram]