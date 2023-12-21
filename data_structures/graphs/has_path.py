graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def hasPath(graph, source, target):
    if target in graph[source]:
        return True

    for neighbor in graph[source]:
        if hasPath(graph, neighbor, target) == True:
            return True

    return False

#Bad solution in time complexity O(N²)
def breadthHasPathStack(graph, source, target):
    queue = [source]
    
    while queue:
        current = queue.pop(0)
        if target == current: return True
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False
        
    
print(breadthHasPathStack(graph, 'd', 'e'))