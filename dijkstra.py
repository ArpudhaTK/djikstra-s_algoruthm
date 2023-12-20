def dijkstra_shortest_path(graph, source):
    n = len(graph) - 1  # Adjust the size of the graph
    S = set()
    max_value = float('inf')  # A substitute for sys.maxsize
    D = {i: max_value for i in range(1, n + 1)}
    D[source] = 0

    for _ in range(1, n):
        u = min((v for v in range(1, n + 1) if v not in S), key=lambda x: D[x])
        S.add(u)

        for v in range(1, n + 1):
            if v not in S and graph[u][v] != 0:
                D[v] = min(D[v], D[u] + graph[u][v])

    return D

# Example usage:
n = 5  # Replace with your desired value of n
graph = [[0] * (n + 1) for _ in range(n + 1)]  # Adjust the size of the graph

# Initialize your graph here

# Example graph representation
graph = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 2, 4, 1, 3],
    [0, 2, 0, 1, 3, 2],
    [0, 4, 1, 0, 6, 5],
    [0, 1, 3, 6, 0, 4],
    [0, 3, 2, 5, 4, 0]
]

source_vertex = 1  # Replace with your desired source vertex

shortest_paths = dijkstra_shortest_path(graph, source_vertex)
print("Shortest paths from vertex", source_vertex, "to all other vertices:", shortest_paths)
