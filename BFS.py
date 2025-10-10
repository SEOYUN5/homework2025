# 6. 너비 우선 탐색 (Breadth-First Search, BFS)
from collections import deque

mygraph = {
    "A": ["B", "C"],
    "B": ["D", "E", "A"],
    "C": ["F", "A"],
    "D": ["B"],
    "E": ["G", "H", "B"],
    "F": ["H", "C"],
    "G": ["E"],
    "H": ["E", "F"]
}

def bfs(graph, start):
    visited = {start}
    que = deque()
    que.append(start)

    print("BFS : ", end='')

    while que:
        v = que.popleft()

        print(v, end=' ')

        nbr = [u for u in graph[v] if u not in visited]

        for u in nbr:
            visited.add(u)
            que.append(u)

    print()

bfs(mygraph, "A")
