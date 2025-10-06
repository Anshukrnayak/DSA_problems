from collections import deque

def dfs(node,adj,visited,result):
    visited.add(node)
    result.append(node)

    for n in adj[node]:
        if n not in visited:
            dfs(n,adj,visited,result)
    return result

adjacency_list = [
    [],
    [2,4],
    [1,3,6],
    [2],
    [1,5,7],
    [4,8],
    [2],
    [4,8],
    [5,7]
]


