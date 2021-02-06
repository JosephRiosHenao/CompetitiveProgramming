raw_input = '0' #input 

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    Output = list()
    for i in range(0, z+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if ((i+j+k)!=n): Output.append([i,j,k])
    print(Output)
