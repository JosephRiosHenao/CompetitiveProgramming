from typing import List

def test_generic(data:List[int]):
    idx:int
    for idx in range(0,len(data)-1):
        assert(data[idx] < data[idx+1], 'Test failed!')
    return True