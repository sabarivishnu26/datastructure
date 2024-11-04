import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph):
    V = len(graph)
    mst_set = [False] * V
    edge_heap = [(0, 0)]
    mst_edges = []
    total_weight = 0

    while edge_heap:
        weight, u = heapq.heappop(edge_heap)
        if mst_set[u]:
            continue

        mst_set[u] = True
        total_weight += weight

        for v, w in enumerate(graph[u]):
            if not mst_set[v] and w > 0:
                heapq.heappush(edge_heap, (w, v))
                mst_edges.append((u, v, w))

    print("Edge \tWeight")
    for u, v, w in mst_edges:
        print(f"{u} - {v} \t{w}")
    print("Total weight of MST:", total_weight)
    
    return mst_edges

# Graph as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Run Prim's algorithm and get the MST edges
mst_edges = prim_mst(graph)

# Plotting
G = nx.Graph()
for u, v, w in mst_edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
plt.title("Prim's Algorithm MST")
plt.show()
