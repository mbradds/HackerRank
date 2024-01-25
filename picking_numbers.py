#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    maximum=0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        c = c+d
        if c > maximum:
            maximum = c
    return maximum


if __name__ == '__main__':
    a = [4, 6, 5, 3, 3, 1]
    result = pickingNumbers(a)
