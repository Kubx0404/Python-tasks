graph = {
    'A': {'B': 1, 'E': 4},
    'B': {'C': 2, 'F': 6, 'G': 2},
    'C': {'D': 1, 'G': 2},
    'D': {'H': 4, 'G': 1},
    'E': {'F': 5},
    'F': {},
    'G': {'F': 1, 'H': 1},
    'H': {},
}
starting_node = 'A'
path = {}  # shortest distance between all the nodes
adj_node = {}  # explore neighbours
queue = []  # box of unvisited nodes

for node in graph:
    path[node] = float("inf")  # adding every node infinity
    adj_node[node] = None  # adding every node to dictionary of neighbour
    queue.append(node)  # adding every node to queue
path[starting_node] = 0
print(path)
# if graph['F']:
#     print("jestem pełny")

# def dijkstra(graph,source):
#     for vertex in graph:
#         print(vertex)
#
# dijkstra(graph)