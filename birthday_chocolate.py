def birthday(s, d, m):
    c = 0
    chocolate = 0
    possible_lists = []
    while c<= len(s):
        l = s[c:m+c]
        possible_lists.append(l)
        c = c+1
    
    for lis in possible_lists:
        check_sum = sum(lis)
        if check_sum == d:
            chocolate = chocolate+1
    
    return(chocolate)
    
    
s = [2,3,4,4,2,1,2,5,3,4,4,3,4,1,3,5,4,5,3,1,1,5,4,3,5,3,5,3,4,4,2,4,5,2,3,2,5,3,4,2,4,3,3,4,3,5,2,5,1,3,1,4,2,2,4,3,3,3,3,4,1,1,4,3,1,5,2,5,1,3,5,4,3,3,1,5,3,3,3,4,5,2]
d = 26
m = 8
x = birthday(s,d,m)
print(x)