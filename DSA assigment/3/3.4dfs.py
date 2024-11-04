import networkx as nx 
import matplotlib.pyplot as plt 
def dfs(graph, start, visited=None, dfs_edges=[]):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_edges.append((start, neighbor))
            dfs(graph, neighbor, visited, dfs_edges)
    return dfs_edges

# DFS traversal from node 0
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 3)]
G.add_edges_from(edges)
dfs_edges = dfs(G, 0)

# Plotting DFS
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="orange", node_size=500, edge_color="gray")
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="orange", width=2)
plt.title("Depth-First Search (DFS) Traversal")
plt.show()
