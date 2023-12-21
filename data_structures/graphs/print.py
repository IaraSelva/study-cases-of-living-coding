
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def depthFirstPrint(graph, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        
        for next in graph[current]:
            stack.append(next)

def breadthFirstPrint(graph, source):
    queue = [source]
    while queue:
        current = queue.pop(0)
        print(current)

        for next in graph[current]:
            queue.append(next)

def depthFirstPrintRecursive(graph, source):
    print(source)

    current = graph[source]
    for next in current:
        depthFirstPrintRecursive(graph, next)

depthFirstPrint(graph, 'a')
print("\n")
breadthFirstPrint(graph, 'a')
print("\n")
depthFirstPrintRecursive(graph, 'a')
print("\n")
