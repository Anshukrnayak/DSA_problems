from collections import deque

def bfs(adj, starting_node):
    queue = deque()
    seen = set()
    queue.append(starting_node)
    seen.add(starting_node)
    result = []

    while queue:
        e = queue.popleft()  # Use popleft() for FIFO (queue behavior)
        result.append(e)
        for node in adj[e]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
    return result

adjacency_list = [
    [],
    [2, 8],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [1, 7, 9],
    [8]
]

# Same adjacency_list as above
print(bfs(adjacency_list, 1))  # Output: [1, 2, 8, 3, 4, 7, 9, 5, 6]