listScore = []
listNameScore = []
listLowNameScore = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listNameScore.append([name,score])
        listScore.append([score])
    sorted(listScore)
    for i in listScore[:2]:
        for j in range(len(listNameScore)):
            if (i == listNameScore(j,1)): 
                listLowNameScore.append([listNameScore(j,0),listNameScore(j,1)])
    print(listNameScore)
    #print(sorted(listNameScore)) #Lista ordenada por nombres alphabeticamente juntu a su puntuacion
