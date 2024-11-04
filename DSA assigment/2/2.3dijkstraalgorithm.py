import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    dijkstra_edges = []

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                dijkstra_edges.append((current_node, neighbor))
    return distances, dijkstra_edges

# Creating a weighted directed graph for Dijkstra's
G = nx.DiGraph()
edges = [(0, 1, 4), (0, 2, 1), (1, 3, 1), (2, 1, 2), (2, 3, 5)]
G.add_weighted_edges_from(edges)

# Dijkstra's algorithm from node 0
distances, dijkstra_edges = dijkstra(G, 0)

# Plotting
pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightcoral", node_size=500, font_size=10, edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
nx.draw_networkx_edges(G, pos, edgelist=dijkstra_edges, edge_color="red", width=2)
plt.title("Dijkstra's Algorithm Shortest Path")
plt.show()

