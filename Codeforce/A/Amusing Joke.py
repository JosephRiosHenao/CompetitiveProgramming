# https://codeforces.com/problemset/problem/141/A
guest, door, pile_input = input(), input(), input()

def delete_in_string(string, pile):
    for letter in string:
        index = pile.find(letter)
        if index == -1: 
            print('NO')
            exit()
        # print(f"eliminando letra {letter} en cadena {pile}")
        pile = pile.replace(letter, '', 1)
    return pile
        
pile = delete_in_string(door, pile_input)
pile = delete_in_string(guest, pile)
if len(pile) == 0:
    print("YES")
else:
    print("NO")

