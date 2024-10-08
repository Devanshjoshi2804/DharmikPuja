def graphColoring(graph, m):
    n = len(graph)
    color = [0] * n

    def isSafe(v, c):
        return all(c != color[i] for i in range(n) if graph[v][i])

    def backtrack(v):
        nonlocal color
        if v == n:
            return True
        for c in range(1, m+1):
            if isSafe(v, c):
                color[v] = c
                if backtrack(v+1):
                    return True
                color[v] = 0
        return False

    if not backtrack(0):
        print("Solution does not exist")
        return False
    print("Solution Exists:")
    print("Following are the assigned colors:")
    print(*color)

graph = []
n = int(input("Enter number of vertices: "))
print("Enter graph:")
for _ in range(n):
    graph.append(list(map(int, input().split())))
m = int(input("Enter number of colors: "))
graphColoring(graph, m)
