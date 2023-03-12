from typing import List

def test_generic(data:List[int]):
    for idx, number in enumerate(data):
        assert number < data[idx+1]
