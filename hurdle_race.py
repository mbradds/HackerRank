#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    highest = max(height)
    if highest >= k:
        return highest - k
    else:
        return 0


if __name__ == '__main__':
    k = 4
    height = [1, 6, 3, 5, 2]
    result = hurdleRace(k, height)
