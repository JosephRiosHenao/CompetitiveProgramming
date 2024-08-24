# https://codeforces.com/contest/1978/problem/A
test_cases = [[int(input()), [int(page) for page in input().split()]] for _ in range(int(input()))]


def calc(books: list):       
    books = books
    pile_one = []
    pile_two = []
    order = [True,False,False,True] 
    position_order = 0
    for book in books:
        if order[position_order] is True:
            pile_one.append(book)
            # print("Organizando page e n pile one ", book)
        else:
            pile_two.append(book)
            # print("Organizando page en pile two ", book)
        if position_order == (len(order)-1): position_order = 0
        else: position_order += 1
    print("Books: ", books)
    print("Pile one: ", pile_one)
    print("Pile two: ", pile_two)
    print(f"Resultado: {pile_one[-1]+pile_two[-1]}")
    # print(f"{pile_one[-1]+pile_two[-1]}")


for test_case in test_cases:
    calc(test_case[1])    