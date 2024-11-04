import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    bfs_edges = []

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                bfs_edges.append((node, neighbor))
    return visited, bfs_edges

# Define the directed graph
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (1, 2)]
G.add_edges_from(edges)

# Perform BFS traversal from node 0
visited_nodes, bfs_edges = bfs(G, 0)

# Plotting the BFS traversal
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=500, font_size=10, edge_color="gray")
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="green", width=2)
plt.title("Breadth-First Search (BFS) Traversal")
plt.show()
