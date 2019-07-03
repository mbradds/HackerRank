
def hourglassSum(arr):
    
    row_count = 0
    hourglasses = []
    while row_count+3 <= len(arr):
        row_list = arr[row_count:row_count+3]
        row_count = row_count+1

        column_count = 0
        while column_count+3 <= len(arr):
            hourglass = []
            for row in row_list:
                hour_glass_part = row[column_count:column_count+3]
                hourglass.append(hour_glass_part)
            hourglasses.append(hourglass)
            column_count = column_count +1
    
    count_list = []
    for hour in hourglasses:
        s = 0
        for n,h in enumerate(hour):
            if n == 0 or n == 2:
                s = s+sum(h)
            else:
                s = s+h[1]
        count_list.append(s)
        
    return(max(count_list))


hourglass = [[1,1,1,0,0,0],
             [0,1,0,0,0,0],
             [1,1,1,0,0,0],
             [0,0,2,4,4,0],
             [0,0,0,2,0,0],
             [0,0,1,2,4,0]]

print(hourglassSum(hourglass))

#%%

