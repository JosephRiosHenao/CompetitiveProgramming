# https://codeforces.com/problemset/problem/263/A
matriz = [input() for _ in range(5)]
position = [[idx+1, row.split().index("1")+1] for idx, row in enumerate(matriz) if "1" in row][0]
print(abs(3-position[1])+abs(3-position[0]))

