from query import QueryInt
from test_query import test_generic


for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, query)
        plt.clf()
        if query[j] > query[j+1]:
            query[j], query[j+1] = query[j+1], query[j]



def main():
    
    AMOUNT = 1000
    MIN_VALUE = 0
    MAX_VALUE = 100
    STEPS = 1
    
    data = QueryInt(AMOUNT,MIN_VALUE,MAX_VALUE,STEPS).calculate()
    while test_generic(data):
        print("Iteracion")
        data = algorithm(data)

if __name__ == "__main__":
    main()