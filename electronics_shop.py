#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    def budget_filter(numbers, b):
        return [x for x in numbers if x <= b]

    keyboards = budget_filter(keyboards, b)
    drives = budget_filter(drives, b)
    
    combinations = []
    for k in keyboards:
        for d in drives:
            combinations.append(k + d)
    
    combinations = budget_filter(combinations, b)
    combinations = sorted(combinations, reverse = True)
    if (len(combinations) == 0):
        return -1
    else:
        return combinations[0]

if __name__ == '__main__':
    b = 5
    keyboards = [4]
    drives = [5]
    moneySpent = getMoneySpent(keyboards, drives, b)
