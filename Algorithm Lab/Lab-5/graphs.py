from collections import deque

graphs = {
    's': set(["a", "b", "c"]),
    'a': set(["s", "d"]),
    'b': set(["s", "e"]),
    'c': set(["f"]),
    'd': set(["a"]),
    'e': set(["b", "g"]),
    'f': set(["c"]),
    'g': set(["e"])
}

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            adjacent = sorted(adjacents for adjacents in graph[vertex] if adjacents not in visited)
            queue.extend(adjacent)

    print(visited)

bfs(graphs, 's')