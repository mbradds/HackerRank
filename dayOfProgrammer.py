import math
import os
import random
import re
import sys
#%%
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    
    if year >= 1700 or year <= 2700:
        
        #Julian
        if year <= 1917:
            #check if divisible by 4
            if year%4 == 0:
                feb = 28
            else:
                feb = 29
        
        #Gregorian
        elif year >= 1919:
            
            if (year%400 == 0) or (year%4==0 and year%100 != 0):
                feb = 29
            else:
                feb = 28
        else:
            None #Year = 1918
        
        callendar = [31,feb,31,30,31,30,31,31,30,31,30,31]
        programmer = 256
        m = 0
        for ind,val in enumerate(callendar):
            m = val+m
            if m > programmer:
                break
        
        day = programmer - sum(callendar[:ind])
        month = ind+1
        
        date = str(day)+'.'+'0'+str(month)+'.'+str(year)
        
        return(date)
    else:
        return(None)
    

#%%
        

year = dayOfProgrammer(2017)
