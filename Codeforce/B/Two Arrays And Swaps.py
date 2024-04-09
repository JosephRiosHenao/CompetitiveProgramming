# https://codeforces.com/problemset/problem/1353/B
def obtain_swap_arrays():
    return [list(map(int,input().split())), [list(map(int,input().split())) for _ in [1,2]]]
test_cases = [obtain_swap_arrays() for _ in range(int(input()))]
[case.sort(reverse=True) for test_case in test_cases for case in test_case[1]]
for test_case in test_cases:
    calc_case = list(test_case[1][0]+test_case[1][1][:test_case[0][1]])
    calc_case.sort(reverse=True)
    print(max(0, max([sum(test_case[1][0]),sum(calc_case[:test_case[0][0]])])))

# if test_case[0][1] == 0: 
#     print(sum(test_case[1][0])) 
# else:
#     cases = [0,sum(test_case[1][0])]
#     for inum_case in range(0 if test_case[0][0]-test_case[0][1]==0 else test_case[0][0]-1,
#                             test_case[0][0] if test_case[0][0]-test_case[0][1]==0 else 0,
#                             1 if test_case[0][0]-test_case[0][1]==0 else -1):
#         num_case = test_case[1][0][inum_case]
#         if num_case < test_case[1][1][0]:
#             cases.append(sum(test_case[1][0][:inum_case]+test_case[1][1][:test_case[0][0]-inum_case]))
#             if num_case==test_case[0][1]: break
#         elif test_case[0][0]-inum_case < test_case[0][0] and test_case[1][0][test_case[0][0]-inum_case] < test_case[1][1][0]:
#             cases.append(sum(test_case[1][0][:test_case[0][0]-inum_case]+test_case[1][1][:test_case[0][0]-len(test_case[1][0][:test_case[0][0]-inum_case])]))
#     print(max(0,max(cases)))

# [print(max(0,sum(test_case[1][0][:test_case[0][0]-test_case[0][1]]+test_case[1][1][:test_case[0][1]]),
#             sum(test_case[1][1][:test_case[0][0]-test_case[0][1]]+test_case[1][0][:test_case[0][1]]),
#             sum(test_case[1][0]), sum(test_case[1][0]) if test_case[0][1]==test_case[1][1] else 0 )) 
#             if test_case[0][1] != 0
#             else print(sum(test_case[1][0]))
#             for test_case in test_cases]

# [print(max(0,sum(test_case[1][0][:test_case[0][0]-test_case[0][1]]+test_case[1][1][:test_case[0][1]]),
#             sum(test_case[1][1][:test_case[0][0]-test_case[0][1]]+test_case[1][0][:test_case[0][1]]),
#             sum(test_case[1][0]), sum(test_case[1][0]) if test_case[0][1]==test_case[1][1] else 0 )) 
#             if test_case[0][1] != 0
#             else print(sum(test_case[1][0]))
#             for test_case in test_cases]
