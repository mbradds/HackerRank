import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sock_holder = {}
    for sock in ar:
        if sock in sock_holder:
            sock_holder[sock].append(sock)
        else:
            sock_holder[sock] = [sock]
    
    pairs = 0
    for key, value in sock_holder.items():
        if len(value) >= 2:
            pairs = pairs + len(value)//2
        
    return pairs

if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n=7, ar=ar)