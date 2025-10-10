#5. 깊이 우선 탐색
mygraph = {
    "A": ["B", "C"],
    "B": ["D", "C", "A", "E"],
    "C": ["F", "B", "A"],
    "D": ["B"],
    "E": ["H", "G", "B"],
    "F": ["G", "C", "H"],
    "G": ["E", "F"],
    "H": ["E", "F"]
}

def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')

        nbr = [v for v in graph[start] if v not in visited]

        for v in nbr:
            dfs(graph, v, visited)

print("DFS : ", end='')
dfs(mygraph, "A", set())
print()
