if __name__ == '__main__':
    a,b=0,0
    Ciclo = True
    while Ciclo:
        a = float(input("Digite un numero "))
        b = float(input("Digite por cuanto lo dividira "))
        if a == 0 or b == 0:
            print("No se puede realizar una division entre 0")
        else:
            Ciclo = False
    print(a//b)
    print(a/b)