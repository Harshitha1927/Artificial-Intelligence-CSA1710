from itertools import permutations

cost = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

best = 9999

for p in permutations([1,2,3]):
    path = (0,) + p + (0,)
    total = sum(cost[path[i]][path[i+1]] for i in range(4))
    
    if total < best:
        best = total
        route = path

print("Best Route:", route)
print("Minimum Cost:", best)
