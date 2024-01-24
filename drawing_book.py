import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    page_turns = math.floor(n/2)
    left_turns = math.floor(p/2)
    right_turns = page_turns - left_turns
    
    if right_turns > left_turns:
        return left_turns
    else:
        return right_turns

if __name__ == '__main__':
    n = 6
    p = 4
    result = pageCount(n, p)