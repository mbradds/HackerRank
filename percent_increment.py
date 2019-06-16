'''
this is a custom algorithm for a problem at work.

Problem:
    You have an array of decimals, each between one and zero, and they all add up to one. The decimals represent percentages.
    For each decimal individually, you need to increment each by 0.1 (one percent) until it reaches 100. Meanwhile, all the other
    percentages need to be decreased by a corresponding amount, while staying above zero, so that all the percentages equal 1,
    or 100 percent.
    
Inputs:
    An array of integers, each between one and zero

Outputs:
    A list fof lists containing each variation of the percentages
'''

def percent_increment(percentages,increment=0.01):
    
    results = []
    
    for percent in percentages:
        
        up_val = percent 
        i = 0
        zeroes = 0
        zero_list = []
        allocation = 0
        
        while up_val+i < 1:
            
            i = i+increment
            current_results = []
            share = (i-allocation)/((len(percentages)-1)-zeroes)
            
            
            for p in percentages:
                    
                if p == percent:
                    current_results.append(up_val+i)
                elif p-share > 0:
                    current_results.append(p-share)
                else:
                    if p not in zero_list:
                        zero_list.append(p)
                        allocation = allocation+p
                        
                    zeroes = len(zero_list)
                    current_results.append(0)
                    
            #print(current_results,sum(current_results))
                    
            results.append(current_results)
            
    return(results)
    
    return(None)

p = [0.6,0.13,0.06,0.21]
increment = 0.05
x = percent_increment(p,increment)
