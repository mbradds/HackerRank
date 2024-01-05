s = "1222222556888888"

def comp(s):
    s = [int(x) for x in str(s)]
    holder = []
    new = True
    for index, value in enumerate(s):
        if new:
            current = [1, value]
        if index+1 < len(s):
            next_value = s[index+1]
            if next_value == value:
                current[0] = current[0]+1
                new = False
            else:
                new = True
                holder.append(current)
        else:
            holder.append(current)
    
    print(' '.join(str(tuple(x)) for x in holder))
    return holder



x = comp(s)
