# https://codeforces.com/problemset/problem/271/A
init_year = input()
year = init_year
while True:
    cont_dont_repeat = 0
    for alpha in year: 
        if year.count(alpha) > 1 or init_year==year:
            break
        else:
            cont_dont_repeat += 1
    if cont_dont_repeat == len(year): 
        print(year)
        break
    year = str(int(year)+1)