from typing import List


class BubbleSort():
    def calculate(self, query:List[int]):
        n = len(query)                
        for j in range(n-1):  
            if(query[j]>query[j+1]):   
                query[j],query[j+1] = query[j+1], query[j]  
        return query
