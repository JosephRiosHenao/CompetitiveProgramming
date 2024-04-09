# https://codeforces.com/problemset/problem/1353/B
def obtain_swap_arrays():
    return [list(map(int,input().split())), [list(map(int,input().split())) for _ in [1,2]]]
test_cases = [obtain_swap_arrays() for _ in range(int(input()))]
[case.sort(reverse=True) for test_case in test_cases for case in test_case[1]]
for test_case in test_cases:
    calc_case = list(test_case[1][0]+test_case[1][1][:test_case[0][1]])
    calc_case.sort(reverse=True)
    print(max(0, max([sum(test_case[1][0]),sum(calc_case[:test_case[0][0]])])))