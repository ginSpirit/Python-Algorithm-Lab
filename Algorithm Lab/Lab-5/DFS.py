graph = {
    's': ['a', 'b', 'c'],
    'a': ['s', 'd'],
    'b': ['s', 'e'],
    'c': ['f'],
    'd': ['a'],
    'e': ['b', 'g'],
    'f': ['c'],
    'g': ['e']
}

visited = set()

def dfs(node):
    visited.add(node)
    yield node
    for neighbor in graph[node]:
        if neighbor not in visited:
            yield from dfs(neighbor)

start = 's'
print(list(dfs(start)))