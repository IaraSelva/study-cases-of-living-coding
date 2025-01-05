def has_path(source, destination, graph, visited=set()):
    if source not in graph: return False
    if destination in graph[source]: return True
    if source in visited: return False
    visited.add(source)

    for neighbor in graph[source]:
        if has_path(neighbor, destination, graph, visited): return True
    return False

graph = {
  "f": ['g', 'i'],
  "g": ['h'],
  "h": [],
  "i": ['g', 'k'],
  "j": ['i'],
  "k": []
}
'''print(has_path("f", "k", graph))
print(has_path("f", "j", graph))
print(has_path("i", "h", graph))

graph = {
  "v": ['x', 'w'],
  "w": [],
  "x": [],
  "y": ['z'],
  "z": [],  
}
print(has_path("v", "w", graph))
print(has_path("v", "z", graph))'''

def undirected_path(edges, node_A, node_B):
    graph = make_graph(edges)
    
    return find_path(graph, node_A, node_B, set())

def find_path(graph, node_A, node_B, visited):
    if node_B in graph[node_A]: return True
    if node_A in visited: return False
    visited.add(node_A)

    for neighbor in graph[node_A]:
        if find_path(graph, neighbor, node_B, visited): return True
    return False
 
def make_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

'''print(undirected_path(edges, 'j', 'm'))
print(undirected_path(edges, 'm', 'j'))
print(undirected_path(edges, 'l', 'm'))
print(undirected_path(edges, 'k', 'o'))
print(undirected_path(edges, 'i', 'o'))

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

print(undirected_path(edges, 'a', 'b'))
print(undirected_path(edges, 'a', 'c'))
print(undirected_path(edges, 'r', 't'))
print(undirected_path(edges, 'r', 'b'))'''

def connected_components_count(graph):
    response = {}
    count = 0
    global_visited = set()

    for node in graph:
        curr_visited = explore(graph, node, global_visited, set())
        if curr_visited:
            count += 1
            response[count] = curr_visited
    return response

def explore(graph, node, visited, curr_visited):
    if node in visited: return
    visited.add(node)
    curr_visited.add(node)

    for neighbor in graph[node]:
        explore(graph, neighbor, visited, curr_visited)

    return curr_visited

'''print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))

print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}))

print(connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}))

print(connected_components_count({}))

print(connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}))'''

def largest_component(graph):
    largest = 0
    visited = set()
    response = {}
    largest_visited = set()

    for node in graph:
        curr_visisted = set()
        curr_size = get_size(graph, node, visited, curr_visisted)
        if curr_size > largest:
            largest = curr_size
            largest_visited = curr_visisted
    response[largest] = largest_visited
    return response
        
def get_size(graph, node, visited, curr_visited):
    if node in visited: return 0
    visited.add(node)
    curr_visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += get_size(graph, neighbor, visited, curr_visited)
    return size

'''print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))'''

from collections import deque

def shortest_path(edges, source, target):
    graph = make_graph(edges)
    visited = set()

    queue = deque([(source, 0)])

    while queue:
        node, distance = queue.popleft()
        visited.add(node)

        if node == target: return distance

        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance+1))
    return -1

'''edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))
print(shortest_path(edges, 'y', 'x'))

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
print(shortest_path(edges, 'a', 'e'))
print(shortest_path(edges, 'e', 'c'))
print(shortest_path(edges, 'b', 'g'))

edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

print(shortest_path(edges, 'w', 'e'))'''



def build_directed_graph(edges):
    graph = {}
    for node, neighbor in edges:
        if node not in graph:
          graph[node] = []
        graph[node].append(neighbor)
    print(graph)
    return graph

def find_n_connected_components(n, edges):
    graph = build_directed_graph(edges)
    count = 0
    visited = set()
    
    for node in graph:
        if node not in visited:
          result = explore(graph, node, visited)
          count += result
    return count

def explore(graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    if node not in graph: return 0
    
    for neighbor in graph[node]:
        explore(graph, neighbor, visited)
    return 1

n = 5
edges = [[0,1],[1,2],[3,4]]
print(find_n_connected_components(n, edges))

n = 8
edges = [[1,2],[1,3],[2,3],[7,5],[5,4],[6,8]]
print(find_n_connected_components(n, edges))