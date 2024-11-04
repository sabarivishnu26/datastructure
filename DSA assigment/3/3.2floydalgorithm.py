import networkx as nx
import matplotlib.pyplot as plt

def floyd_warshall(graph):
    nodes = list(graph.nodes)
    dist = {node: {n: float('inf') for n in nodes} for node in nodes}
    
    # Set distance from each node to itself to 0
    for node in nodes:
        dist[node][node] = 0
    
    # Initialize distances based on direct edges
    for u, v, weight in graph.edges(data='weight'):
        dist[u][v] = weight
    
    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Graph setup
G = nx.DiGraph()
edges = [(0, 1, {'weight': 4}), (0, 2, {'weight': 1}), (1, 3, {'weight': 1}),
         (2, 1, {'weight': 2}), (2, 3, {'weight': 5})]
G.add_edges_from(edges)

# Apply Floyd-Warshall algorithm
floyd_distances = floyd_warshall(G)

# Display the result
print("All-pairs shortest path distances:")
for source, targets in floyd_distances.items():
    print(f"{source}: {targets}")

# Plotting the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="gray")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Directed Graph with Edge Weights")
plt.show()
