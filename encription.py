#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    s_length = len(s)
    s_sqrt = math.sqrt(s_length)
    rows = math.floor(s_sqrt)
    cols = rows+1
    size = rows*cols
    
    if size < s_length:
        incorrect_size = True
        while incorrect_size:
            rows = rows+1
            size = rows*cols
            if size < s_length:
                incorrect_size = True
            else:
                incorrect_size = False
    

    arr = [[] for x in range(cols)]
    for x in range(rows):
        sliced = s[:cols]
        for index, value in enumerate(sliced):
            arr[index].append(value)
        s = s[cols:]
        
    string = ["".join(x) for x in arr]
    return " ".join(string)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = "chillout"
    result = encryption(s)

    # fptr.write(result + '\n')

    # fptr.close()