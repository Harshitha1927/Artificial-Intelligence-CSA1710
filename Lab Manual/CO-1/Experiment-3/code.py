from collections import deque

cap = (4, 3)
start = (0, 0)
q = deque([start])
visited = {start}

while q:
    a, b = q.popleft()
    print(a, b)

    if a == 2:
        break

    states = [(cap[0],b), (a,cap[1]), (0,b), (a,0)]
    x = min(a, cap[1]-b)
    states.append((a-x,b+x))
    x = min(b, cap[0]-a)
    states.append((a+x,b-x))

    for s in states:
        if s not in visited:
            visited.add(s)
            q.append(s)
