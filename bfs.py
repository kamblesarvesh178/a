graph = {
    '1' : ['2','3'],
    '2' : ['1','4'],
    '3' : ['1','4','5'],
    '4' : ['2','3'],
    '5' : ['3']
}

visited = set()

def dfs(graph,vertex,visited):
    if vertex not in visited:
        visited.add(vertex)
        print(vertex)
        for neighbour in graph[vertex]:
            dfs(graph,neighbour,visited)

dfs(graph,'3',visited)


#ASMT 1 BFS
graph = {
    '1' : ['2'],
    '2' : ['1','3','4'],
    '3' : ['2','5'],
    '4' : ['2'],
    '5' : ['3']
}

visited = set()

def bfs(graph,vertex,visited):
    visited.add(vertex)
    queue = []
    queue.append(vertex)
    
    while queue:
        v = queue.pop(0)
        print(v)
        
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs(graph,'4',visited)