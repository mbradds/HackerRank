def migratoryBirds(arr):
    results = {}
    
    for bird in arr:
        if bird not in results.keys():
            results[bird] = 1
        else:
            results[bird] = results[bird]+1

    most_bird = max(results.values())
    
    figure_max = []
    
    for bird,count in results.items():
        if count == most_bird:
            figure_max.append(bird)
    
    return(min(figure_max))



birds = [1,4,4,4,5,3]
x = migratoryBirds(birds)
print(x)

#print(1 in x.keys)