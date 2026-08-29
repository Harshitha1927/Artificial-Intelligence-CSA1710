from collections import deque

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[], 'E':[], 'F':[]
}

q = deque(['A'])
visited = set()

while q:
    node = q.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        q.extend(graph[node])
