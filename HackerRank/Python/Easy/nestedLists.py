"""listScore = []
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
"""
Students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        Students.append([input(),float(input())])
    second_highest = sorted(list(set([marks for name, marks in Students])))[1]
    print('\n'.join([a for a,b in sorted(Students) if b == second_highest]))