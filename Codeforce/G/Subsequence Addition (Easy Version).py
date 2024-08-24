# https://codeforces.com/problemset/problem/1807/G1
def resolve_test_case(test_case):
    if len(test_case) == 1 and test_case[0] == 1: return True
    if len(test_case) == 1 and test_case[0] != 1: return False
    resolve = 0
    for idproblem, problem in enumerate(test_case):
        for idn1, n1 in enumerate(test_case):
            if idn1==idproblem: continue
            combination = [n1]
            if n1 == problem: resolve+=1;break
            for idn2, n2 in enumerate(test_case):
                if idn2==idproblem or idn2==idn1: continue
                combination.append(n2)
                if sum(combination) == problem:resolve+=1;break  
            if sum(combination) == problem: break  
    return True if resolve == len(test_case) else False

test_cases = [[int(input()), [int(i) for i in input().split()]] for n in range(int(input()))]
for test_case in test_cases: 
    if len(test_case[1]) != 1: test_case[1].sort()
[print("YES") if resolve_test_case(test[1]) else print("NO") for test in test_cases]