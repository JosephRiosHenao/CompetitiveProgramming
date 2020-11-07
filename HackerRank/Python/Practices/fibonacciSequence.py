Limit = (int(input("Digite el numero max para la serie ")))
numAntepasado, numAnterior, numSumado = 1, 1, 0
for numSecuencia in range(Limit):
    numSumado = numAnterior + numAntepasado
    print(f"{numAntepasado} + {numAnterior} = {numSumado}")
    numAntepasado = numAnterior
    numAnterior = numSumado
