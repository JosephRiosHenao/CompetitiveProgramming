# def get_array(): return [int(n) for n in input().split()]
    
# def solve():
    # _ = input()
    # a = get_array(); b = get_array()

# [solve() for _ in range(int(input()))]


    
# def solve():
#     print(2*(int(input())-1))
    
    
#     # lossers_bracket = 0
#     # winners_bracket = 0
#     # plays = 0
#     # winners_bracket = int(input())
#     # while winners_bracket != 1 or lossers_bracket != 0:
#     #     n_bracket_winners = winners_bracket//2
#     #     print(f"Jugadas en el bracket de ganadores: {n_bracket_winners}")
#     #     n_bracket_lossers = lossers_bracket//2
#     #     plays +=

#     #     print(f"Jugadas en el bracket de ganadores: {n_bracket_lossers}")
#     #     winners_bracket -= n_bracket_winners
#     #     lossers_bracket += n_bracket_winners
#     #     lossers_bracket -= n_bracket_lossers
#     #     print(f"Estado en el bracket de ganadores: {winners_bracket}")
#     #     print(f"Estado en el bracket de perdedores: {lossers_bracket}")
#     # print(plays)
    
# [solve() for _ in range(int(input()))]

    
# def solve():
#     n, k = [int(n) for n in input().split()]
#     if k%2 != 0: print("NO"); return
#     print("YES")
#     grid = [["R" if (step+i)%2 == 0 else "L" for step in range(n)] for i in range(n)]
#     temp = 0
#     for step in range(n):
#         if temp < k: temp += 1
#         grid[step][0] = "U"
#     [print("".join(data)) for data in grid]
# [solve() for _ in range(int(input()))]



# for test_case in range(int(input())):
#     n, k = [int(n) for n in input().split()]
#     if k%2 != 0: print("NO"); continue
#     if k>n*n: print("NO"); continue
#     print("YES")
#     grid = [["R" if (step+i)%2 == 0 else "L" for step in range(n)] for i in range(n)]
#     temp = 0
#     for step in range(n):
#         if temp < k: temp += 1
#         grid[step][0] = "U"
#     [print("".join(data)) for data in grid]

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        total_cells = n * n
        
        # Si k == 0 o k == total_cells, es trivial (todas escapan o ninguna)
        if k == 0:
            print("YES")
            for _ in range(n):
                print("L" * n)  # cualquier ciclo cerrado
            continue
        elif k == total_cells:
            print("YES")
            for _ in range(n):
                print("U" * n)  # todas para arriba, todas salen
            continue
        
        # Caso general
        grid = [["L" for _ in range(n)] for _ in range(n)]
        
        # Estrategia: marcar las primeras k celdas (por filas) como 'U' para que escapen,
        # el resto en ciclos cerrados (por ejemplo, todas 'L')
        cnt = 0
        for r in range(n):
            for c in range(n):
                if cnt < k:
                    grid[r][c] = "U"
                    cnt += 1
                else:
                    grid[r][c] = "L"
        
        # Verificar si esta construcción genera exactamente k celdas escapables
        # Solo es válido si los 'U's están alineados con borde o están solos en su columna/fila
        escapable = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 'U' and r == 0:  # en la primera fila, escapan
                    escapable += 1
        
        if escapable == k:
            print("YES")
            for row in grid:
                print("".join(row))
        else:
            print("NO")
solve()

# Para correr localmente, usar:
# if __name__ == "__main__":
#     solve()
