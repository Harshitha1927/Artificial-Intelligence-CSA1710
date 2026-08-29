colors = ['Red', 'Green', 'Blue']

graph = {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B','D'],
    'D':['C']
}

color = {}

def solve(node):
    if node == len(graph):
        return True

    city = list(graph)[node]

    for c in colors:
        if all(color.get(n) != c for n in graph[city]):
            color[city] = c
            if solve(node + 1):
                return True
            del color[city]

    return False

solve(0)
print(color)
