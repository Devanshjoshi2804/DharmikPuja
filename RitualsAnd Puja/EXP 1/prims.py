import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((w, v))
        self.graph[v].append((w, u))

    def prim_mst(self):
        visited = [False] * self.V
        pq = [(0, 0)]
        mst = []

        while pq:
            weight, vertex = heapq.heappop(pq)
            if not visited[vertex]:
                visited[vertex] = True
                mst.append((weight, vertex))
                for w, v in self.graph[vertex]:
                    if not visited[v]:
                        heapq.heappush(pq, (w, v))

        return mst[1:]


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Edges of MST using Prim's Algorithm:")
print(g.prim_mst())
