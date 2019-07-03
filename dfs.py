def dfs_visit(graph, vertex, parents):
    for n in graph[vertex]:
        if n not in parents:
            parents[n] = vertex
            dfs_visit(graph, n, parents)


def dfs(graph, vertex):
    parents = {vertex: None} #tracks visited nodes
    dfs_visit(graph, vertex, parents)


    
graph = {
        'A': ['B','C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
        }

b = dfs(graph,'A')
print(b)

