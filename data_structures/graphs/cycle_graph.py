edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
    ['o', 'i'],
    ['n', 'i']
]

graph = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}

def makeGraph(edges):
    graph = {}

    for edge in edges:
        [a, b] = edge
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def findPath(edges, source, target, check = set()):
    graph = makeGraph(edges)

    if target in graph[source]: return True
    if source in check: return False
    check.add(source)

    for neighbor in graph[source]:
        if findPath(edges, neighbor, target, check) == True:
            return True
    return False

def countConected(graph):
    count = 0

    for node in graph:
        if exploreNodes(graph, node) == True:
            count += 1
    return count

def exploreNodes(graph, node, check = set()):
    if node in check: return False
    check.add(node)
    
    for neighbor in graph[node]:
        exploreNodes(graph, neighbor, check)
    
    return True

def biggestGraph(graph):
    biggest = 0
    for node in graph:
        size = countElements(graph, node)
        if size > biggest: biggest = size
    return biggest

def countElements(graph, node, visited = set()):

    if node in visited: return 0
    visited.add(node)
    size = 1

    for neighbor in graph[node]:
        size += countElements(graph, neighbor, visited)
    
    return size

        
    




print(makeGraph(edges))
#print("\n")
#print(findPath(edges, 'i', 'm'))
#print(findPath(edges, 'j', 'o'))
#print("\n")
#print(countConected(makeGraph(edges)))
print(biggestGraph(graph))