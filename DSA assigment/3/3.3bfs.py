from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = deque([start])
    bfs_edges = []
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                bfs_edges.append((node, neighbor))
    return bfs_edges

# BFS traversal from node 0
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 3)]
G.add_edges_from(edges)
bfs_edges = bfs(G, 0)

# Plotting BFS
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=500, edge_color="gray")
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="green", width=2)
plt.title("Breadth-First Search (BFS) Traversal")
plt.show()
