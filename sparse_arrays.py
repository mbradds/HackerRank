
def matchingStrings(strings, queries):
    
    matching = []
    
    for q in queries:
        query_count = 0
        for string in strings:
            if string == q:
                query_count = query_count+1
        matching.append(query_count)
    
    return(matching)


strings = ['aba','baba','aba','xzxb']
queries = ['aba','xzxb','ab']

arr = matchingStrings(strings,queries)
