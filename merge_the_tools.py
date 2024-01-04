def merge_the_tools(string, k):
    # your code goes here
    n_groups = int(len(string)/k)
    lists = []
    for i in range(n_groups):
        lists.append(list(string[:k]))
        string = string[k:]
    
    new_lists = [[] for x in range(n_groups)]
    for index, l in enumerate(lists):
        for value in l:
            if value not in new_lists[index]:
                new_lists[index].append(value)
    
    for l in new_lists:
        print("".join(l))
    return lists

if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "hello"
    k = 1
    merge_the_tools(string, k)