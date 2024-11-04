import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, node, visited=None, edges=None):
    if visited is None:
        visited = set()
    if edges is None:
        edges = []
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            edges.append((node, neighbor))
            dfs(graph, neighbor, visited, edges)
    return visited, edges

# Creating a directed graph
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
G.add_edges_from(edges)

# DFS traversal from node 0
visited_nodes, dfs_edges = dfs(G, 0)

# Plotting
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, edge_color="gray")
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="blue", width=2)
plt.title("Depth-First Search (DFS) Traversal")
plt.show()
