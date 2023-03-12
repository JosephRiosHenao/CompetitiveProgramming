import pyxel

WIDTH = 100
HEIGHT = 100

class App(object):
    def __init__(self) -> None:
        pyxel.init(WIDTH, HEIGHT)
        pyxel.run(self.update, self.draw)

    __instance = None        
    def __new__(cls):
        if App.__instance is None:
            print("Create instance App")
            App.__instance = object.__new__(cls)
        return App.__instance 
        
    def update(self) -> None:
        pass    
    
    def draw(self) -> None:
        pass