import pyxel
from preset_data import Preset
from time import sleep

class App(object):
    
    def __init__(self) -> None:
        self.objs = []
        
    def start_monitor(self) -> None:
        pyxel.init(Preset.WIDTH, Preset.HEIGHT)
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