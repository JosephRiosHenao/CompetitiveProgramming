# https://codeforces.com/problemset/problem/4/C
test_cases = [input().strip() for _ in range(int(input()))]
test_cases_dict = {}
for test_case in test_cases:
    print('OK') if test_cases_dict.get(test_case,0)==0 else print(f"{test_case}{test_cases_dict.get(test_case)}")
    test_cases_dict[test_case] = test_cases_dict.get(test_case, 0) + 1
