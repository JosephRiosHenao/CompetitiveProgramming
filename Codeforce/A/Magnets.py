# https://codeforces.com/problemset/problem/344/A
magnets = [input() for n in range(int(input()))]
magnet_chain = "".join(magnets)
print(magnet_chain.count("00")+magnet_chain.count("11")+1)