#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    counter = 0
    valleys = 0
    in_valley = False
    
    for step in path:
        if step == "U":
            counter = counter + 1
        else:
            counter = counter - 1
        
        if counter < 0:
            in_valley = True
        
        if in_valley and counter == 0:
            in_valley = False
            valleys = valleys +1
    return valleys

if __name__ == '__main__':
    steps = 8
    path = "UDDDUDUU"
    result = countingValleys(steps, path)
