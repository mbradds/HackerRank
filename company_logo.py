import math
import os
import random
import re
import sys


def create_logo(name):
    holder = {}
    for char in name:
        if char in holder:
            holder[char] = holder[char] + 1
        else:
            holder[char] = 1
    
    sorted_holder = {}
    for key, value in holder.items():
        
        if value in sorted_holder:
            sorted_holder[value].append(key)
        else:
            sorted_holder[value] = [key]
    
    sorted_holder = {key: sorted_holder[key] for key in sorted(sorted_holder.keys(), reverse=True)}
    found_list = []
    for key, value in sorted_holder.items():
        for i in sorted(value):
            found_list.append([key, i])
            
    found_list = found_list[:3]
    for f in found_list:
        print(f[-1], f[0])        


if __name__ == '__main__':
    #s = input()
    s = "aabbbccde"
    h = create_logo(s)