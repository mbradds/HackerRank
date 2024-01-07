def print_rangoli(size):
    a = "abcdefghijklmnopqrstuvwxyz"
    mid = a[size+1]
    lines = []
    # your code goes here
    for letter in a[:size]:
        print(letter)
    return None

if __name__ == '__main__':
    # n = int(input())
    n = 3
    print_rangoli(n)