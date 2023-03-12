import matplotlib.pyplot as plt
import numpy as np
from main import App
from typing import List

class QueryInt():
    def __init__(self, amount:int, min_value:int, max_value:int, steps:int) -> None:
        self.amount:int = amount
        self.min_value:int = min_value
        self.max_value:int = max_value
        self.steps:int = steps
        self.query:List[int] = self.calculate()
        self.longitude:int = len(self.query)
        
    def calculate(self) -> List[int]:
        query:List[int] = np.random.randint(self.min_value,self.max_value, size=self.amount)
        return query
    
    def calculate_padding(self) -> int:
        return np.arange(self.min_value, self.amount, self.max_value)