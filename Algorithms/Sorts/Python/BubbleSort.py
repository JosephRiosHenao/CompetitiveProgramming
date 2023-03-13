from query import QueryInt
from test_query import test_generic
from visualizer_columns import Frame
from main import App
from preset_data import Preset
from typing import List

def calculate(query:List[int]):
    dataset:List[int] = query
    steps = []
    
    n = len(dataset)

                
    for i in range(0,n-1):  
        steps.append(list(dataset))
        for j in range(n-1):  
            if(dataset[j]>dataset[j+1]):   
                dataset[j],dataset[j+1] = dataset[j+1], dataset[j]  
    return steps, dataset



def main():
    
    data = QueryInt(Preset.AMOUNT,Preset.MIN_VALUE,Preset.MAX_VALUE,Preset.STEPS).calculate()    
    steps,dataset = calculate(data)
    print(dataset)
    app = App()
    app.objs.append(Frame(steps))
    app.start_monitor()
if __name__ == "__main__":
    main()