import heapq

graph = {
    'A': [('B',1),('C',3)],
    'B': [('D',2)],
    'C': [('D',1)],
    'D': []
}

h = {'A':4, 'B':2, 'C':1, 'D':0}

pq = [(h['A'], 0, 'A')]
visited = set()

while pq:
    f,g,node = heapq.heappop(pq)

    if node in visited:
        continue

    print(node, end=" ")
    visited.add(node)

    if node == 'D':
        print("\nGoal Reached")
        break

    for nxt,cost in graph[node]:
        heapq.heappush(pq, (g+cost+h[nxt], g+cost, nxt))
