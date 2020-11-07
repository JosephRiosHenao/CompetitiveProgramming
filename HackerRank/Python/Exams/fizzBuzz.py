#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):

    for i in range(n+1):
        if i >= 1:
            if ((i%3) == 0 and (i%5) != 0):
                print("Fizz")
                
            elif ((i%5) == 0 and (i%3) != 0):
                print("Buzz")
                
            if ((i%3) == 0 and (i%5) == 0):
                print("FizzBuzz")
                
            if ((i%3) != 0 and (i%5) != 0):
                print(f"{i}")
    # Write your code here
    
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
