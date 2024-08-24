import pyxel
from Engine.preset_data import Preset
from Engine.query import QueryInt
from Engine.visualizer_columns import VisualizarEngine

from BubbleSort import BubbleSort, SelectionSort, MergeSort


class App(object):
    
    def __init__(self) -> None:
        self.objs = []
        
    def start_monitor(self) -> None:
        pyxel.init(Preset.WIDTH, Preset.HEIGHT, fps=Preset.SPEED)
        pyxel.run(self.update, self.draw)
        

    __instance = None        
    def __new__(cls):
        if App.__instance is None:
            print("Create instance App")
            App.__instance = object.__new__(cls)
        return App.__instance 
        
    def update(self) -> None:
        for obj in self.objs:
            obj.update()
    
    def draw(self) -> None:
        pyxel.cls(0)
        for obj in self.objs:
            obj.draw()
            
def main():
    data = QueryInt(Preset.AMOUNT,Preset.MIN_VALUE,Preset.MAX_VALUE,Preset.STEPS).calculate()    
    algorithm = MergeSort() 
    app = App()
    app.objs.append(VisualizarEngine(data, algorithm))
    app.start_monitor()
if __name__ == "__main__":
    main()