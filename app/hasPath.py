class Graph:
    def __init__(self, input: list):
        self.graph = {}
        for (a, b) in input:
            self.graph[a] = self.graph.get(a, []) + [b]

    def has_path(self, start, end, graph=None, visited=None):
        if not graph:
            graph = self.graph
        if not visited:
            visited = set()

        if start == end:
            return True

        if start not in graph or start in visited:
            return False
        
        visited.add(start)
        
        for neighbor in graph[start]:
            if self.has_path(neighbor, end, graph, visited):
                return True
        return False
    

# {
    # "USD": ["EUR", "GBP"],
    # "EUR": ["JPY", "USD"],
    # "GBP": ["INR"],
    # "BRL": [""]
# }

# edges = [["USD", "EUR"], ["USD", "GBP"], ["EUR", "JPY"], ["EUR", "USD"], ["GBP", "INR"], ["BRL", ""]]

# graph_class = Graph(edges)
# graph_class.make_graph()
# print(graph_class.graph)
# print(graph_class.has_path("USD", "INR"))
        

        
        
