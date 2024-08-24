from typing import List


class BubbleSort():
    def calculate(self, query:List[int], steps=None):
        n = len(query)                
        for j in range(n-1):  
            if(query[j]>query[j+1]):   
                query[j],query[j+1] = query[j+1], query[j]  
        return query

class SelectionSort():
    def calculate(self, query:List[int], steps=0):
        n = len(query)
        position_minimum = steps
        for j in range(steps,n-1,1):
            if query[position_minimum] > query[j]:
                position_minimum = j
        query[steps], query[position_minimum] = query[position_minimum], query[steps]
        return query
    
class MergeSort():
    def calculate