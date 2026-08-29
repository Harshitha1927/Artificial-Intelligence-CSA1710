from collections import deque

start = (3,3,1)
goal = (0,0,0)
q = deque([start])
visited = {start}

while q:
    m,c,b = q.popleft()
    print(m,c,b)

    if (m,c,b) == goal:
        print("Goal Reached")
        break

    for x,y in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
        nm = m-x if b else m+x
        nc = c-y if b else c+y
        nb = 1-b

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):
                s = (nm,nc,nb)
                if s not in visited:
                    visited.add(s)
                    q.append(s)
