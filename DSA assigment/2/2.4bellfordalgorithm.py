import networkx as nx
import matplotlib.pyplot as plt
def bellman_ford(graph, V, start):
    distances = [float('inf')] * V
    distances[start] = 0
    bellman_ford_edges = []

    for _ in range(V - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                bellman_ford_edges.append((u, v))

    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances, bellman_ford_edges

# Define edges for Bellman-Ford as a list of (u, v, weight)
edges = [
    (0, 1, 4), (0, 2, 1),
    (2, 1, 2), (1, 3, 1),
    (2, 3, 5)
]
V = 4

# Bellman-Ford algorithm from node 0
distances, bellman_ford_edges = bellman_ford(edges, V, 0)

# Creating a directed graph for visualization
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# Plotting
pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
nx.draw_networkx_edges(G, pos, edgelist=bellman_ford_edges, edge_color="purple", width=2)
plt.title("Bellman-Ford Algorithm Shortest Path")
plt.show()
