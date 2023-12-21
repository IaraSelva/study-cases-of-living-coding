edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

def makeGraph(edges):
    graph = {}
    
    for node in edges:
        [a, b] = node
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def find_min_path(graph, source, target):
    distance = 0
    queue = [[source, distance]]
    visited = set(source)

    while queue:
        [node, distance] = queue.pop(0)
        if node == target: return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
    return -1
            


graph = makeGraph(edges)

print(find_min_path(graph, 'a', 'e'))
    