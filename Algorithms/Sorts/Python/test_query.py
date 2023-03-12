from typing import List

def test_generic(data:List[int]):
    for idx, number in enumerate(data):
        if number < data[idx+1]: break
        return True
    return False