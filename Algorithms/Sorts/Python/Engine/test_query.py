from typing import List

data:List[int] = [1,2,5,7,8,9]

def test_generic():
    idx:int
    for idx in range(0,len(data)-1):
        assert(data[idx] < data[idx+1], 'Test failed!')
