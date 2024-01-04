#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    not_had = bill.pop(k)
    had = sum(bill)/2
    if b - had > 0:
        return b - had
    else:
        return "Bon Appetit"

if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # bill = list(map(int, input().rstrip().split()))

    # b = int(input().strip())

    x = bonAppetit(bill=[3, 10, 2, 9], k=1, b=7)