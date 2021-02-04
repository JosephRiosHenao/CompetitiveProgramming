raw_input = "entrada de la pagina"

if __name__ == '__main__':
    N = int(raw_input())
    Output = []
    for i in range(N):
        ip = raw_input().split()
        if ip[0] == 'print':
            print(Output)
        elif ip[0] == 'append':
            Output.append(int(ip[1]))
        elif ip[0] == 'remove':
            Output.remove(int(ip[1]))
        elif ip[0] == 'insert':
            Output.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == 'sort':
            Output.sort()
        elif ip[0] == 'pop':
            Output.pop()
        else:
            Output.reverse()
