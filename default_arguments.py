class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


# queries = int(input())
inputs = 1
#queries = ["odd", 2]
queries = ["even", 3]
#queries = [odd 5]
for _ in range(inputs):
    # stream_name, n = input().split()
    stream_name = queries[0]
    n = int(queries[-1])
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())