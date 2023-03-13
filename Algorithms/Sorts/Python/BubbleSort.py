from query import QueryInt
from test_query import test_generic
from visualizer_columns import Frame
from main import App
from preset_data import Preset
from typing import List

def calculate(query:List[int]):
    steps = []
    
    
    n = len(query)

                
    for i in range(0,n-1):  
        for j in range(n-1):  
            steps.append(query)
            if(query[j]>query[j+1]):   
                query[j],query[j+1] = query[j+1], query[j]  
    print(steps)
    return steps



def main():
    data = QueryInt(Preset.AMOUNT,Preset.MIN_VALUE,Preset.MAX_VALUE,Preset.STEPS).calculate()    
    steps = calculate(data)
    # print(steps)
    app = App()
    app.objs.append(Frame(steps))
    app.start_monitor()
if __name__ == "__main__":
    main()