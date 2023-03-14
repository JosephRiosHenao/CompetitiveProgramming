import pyxel

class Column():
    def __init__(self, x:int, y:int, w:int, h:int, c:int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = c
        
    def draw(self) -> None:
        pyxel.rect(self.x,self.y,
                   self.w,self.h,
                   self.color)
    
    def update(self) -> None: pass
    
    def __str__(self) -> str:
        return f"Position: [{self.x}-{self.y}]\nScale: [{self.w}-{self.h}]"