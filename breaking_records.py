
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def breakingRecords(scores):
    high,low = [],[]
    best,worst = 0,0
    i = 0
    while i < len(scores):
        score = scores[i]
        if i==0:
            high.append(score)
            low.append(score)
        else: 
            if score > high[-1]: 
                best = best+1 
                high.append(score)
            else:
                high.append(high[-1])
            
            if score < low[-1]:
                worst = worst+1
                low.append(score)
            else:
                low.append(low[-1])
            
        i = i+1
    return([best,worst])
    
    
    

s = [10,5,20,20,4,5,2,25,1]
x = breakingRecords(s)
print(x)
#%%
