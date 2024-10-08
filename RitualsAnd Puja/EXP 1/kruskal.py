class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def kruskal_mst(self):
        parent = list(range(self.V))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        mst = []
        for w, u, v in sorted(self.graph):
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, w))

        return mst


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Edges of MST using Kruskal's Algorithm:")
print(g.kruskal_mst())
