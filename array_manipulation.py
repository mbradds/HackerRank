

def arrayManipulation(n, queries):
    
    zeroes = [0 for x in range(0,n+2)]
    
    for q in queries:
        zeroes[q[0]-1] = zeroes[q[0]-1] + q[2]
        zeroes[q[1]] = zeroes[q[1]] - q[2] 
        
    c = 0
    new = []
    while c <= len(zeroes):
        new.append(sum(zeroes[0:c]))
        c = c+1
    
    return(max(new))


n = 5
queries = [[1,2,100],
           [2,5,100],
           [3,4,100]]


mav_val = arrayManipulation(n,queries)

#%%

