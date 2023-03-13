from typing import List
from main import App
from column import Column
from preset_data import Preset


class Frame():
    def __init__(self, frames:List[List[int]]) -> None:
        self.frames = frames
        self.position = [0,0]
        self.step = 0
        self.columns:List[Column] = [] 
        
    def calculate_position(self):
        self.position[0] += Preset.PADDING
        return self.position[0]

    def recreating_frames(self):
        self.position[0] = 0
        columns:List[Column] = []
        for column_value in self.frames[self.step]:
            columns.append(Column(self.calculate_position(),self.position[1], Preset.PADDING, column_value, 11))
        self.columns = columns
    
    def update(self):
        if self.step < len(self.frames)-1:
            self.step += 1 
            self.recreating_frames()
    
    def draw(self):
        for column in self.columns: 
            column.draw()
