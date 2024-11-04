import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        self.edges.sort()
        parent = []
        rank = []
        mst_edges = []
        total_weight = 0

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                mst_edges.append((u, v, weight))
                total_weight += weight
                self.union(parent, rank, x, y)

        print("Edge \tWeight")
        for u, v, weight in mst_edges:
            print(f"{u} - {v} \t{weight}")
        print("Total weight of MST:", total_weight)
        
        return mst_edges

# Example usage
graph = Graph(5)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 6)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 4, 7)
graph.add_edge(3, 4, 9)

# Run Kruskal's algorithm and get the MST edges
mst_edges = graph.kruskal_mst()

# Plotting
G = nx.Graph()
for u, v, w in mst_edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightgreen", edge_color="blue", node_size=500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
plt.title("Kruskal's Algorithm MST")
plt.show()
