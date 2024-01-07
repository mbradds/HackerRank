blocks = [4, 3, 2, 1, 3, 4]


def stacker(blocks):
    stack = None
    can_stack = True
    while len(blocks) != 0:
        left, right = blocks[0], blocks[-1]
        if left > right:
            blocks = blocks[1:]
            next_block = left
        else:
            blocks = blocks[:-1]
            next_block = right
        
        if stack == None:
            stack = next_block
        elif stack < next_block:
            can_stack = False
            break
    
    if can_stack:
        print("Yes")
    else:
        print("No")
        

x = stacker(blocks)