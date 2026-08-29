from collections import deque

start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

q = deque([start])
visited = {start}

while q:
    s = q.popleft()
    if s == goal:
        print("Goal Reached:", s)
        break

    z = s.index(0)
    for m in [-3, 3, -1, 1]:
        n = z + m
        if 0 <= n < 9 and not (z%3 == 0 and m == -1) and not (z%3 == 2 and m == 1):
            x = list(s)
            x[z], x[n] = x[n], x[z]
            x = tuple(x)
            if x not in visited:
                visited.add(x)
                q.append(x)
