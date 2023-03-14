from typing import List
from column import Column
from preset_data import Preset
            
class VisualizarEngine():
    def __init__(self, dataset:List[int], algorithm):
        self.columns = []
        self.step = 0
        self.position = [0,0]
        self.dataset = dataset
        self.n = len(dataset)
        self.algorithm = algorithm
    def reposition(self):
        self.dataset = self.algorithm.calculate(self.dataset)
        self.calculate_columns()
    def calculate_position(self):
        self.position[0] += Preset.PADDING
        return self.position[0]
    def calculate_value(self, value:int) -> int:
        return Preset.HEIGHT*value/Preset.MAX_VALUE
    def calculate_columns(self) -> List[Column]:
        self.position[0] = 0
        columns:List[Column] = []
        for column in self.dataset:
            columns.append(Column(self.calculate_position(),self.position[1], Preset.PADDING, self.calculate_value(column), 11))
        self.columns = columns
    def update(self):
        if self.step <= self.n-1:
            self.reposition()
    def draw(self):
        for column in self.columns:
            column.draw()
