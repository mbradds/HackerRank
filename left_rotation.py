
def left_rotation(d,arr):
    new_list = [0 for x in range(0,len(arr))]
    for position,element in enumerate(arr):
        new_position = position-d
        new_list[new_position] = str(element)
    return(' '.join(new_list))


d = 4 
n = 5
print(left_rotation(d,[1,2,3,4,5])) 


#%%

    