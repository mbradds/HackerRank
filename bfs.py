
def bfs(graph,vertex):
    queue = [vertex]

    visited = {vertex:True}
    
    while queue:
        v = queue[0]
        del queue[0]
        
        for n in graph[v]:
            if n not in visited:
                queue.append(n)
                visited[n] = True
                

def bfs_distance(graph, vertex):
    queue = [vertex]
    level = {vertex: 0}
    parent = {vertex: None}
    i = 1
    while queue:
        v = queue[0]
        del queue[0]
        for n in graph[v]:
            if n not in level:            
                queue.append(n)
                level[n] = i
                parent[n] = v
                
        i = i+1
    return(level, parent)



graph = {
        'A': ['B','C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
        }

b = bfs_distance(graph,'A')
print(b)


#%%

v = {'A':0}

v['B'] = 1