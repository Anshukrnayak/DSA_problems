
n=5 # nodes :
m=6 # Edges :

edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# creating a simple matrix :
matrix=[[0 for _ in range(n+1)] for _ in range(n+1)]

for u,v in edges:
    matrix[u][v]=1
    matrix[v][u]=1


# list store of graph nodes;

graph_list=[[] for _ in range(n+1)]
for u,v in edges:
    graph_list[u].append(v)
    graph_list[v].append(u)

# Dictionary :
dictionary=dict()
for i in range(1,n+1):
    dictionary[i]=[]

for u,v in edges:
    dictionary[u].append(v)
    dictionary[v].append(u)

print(dictionary)