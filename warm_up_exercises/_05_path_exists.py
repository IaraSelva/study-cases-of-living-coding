# 5. Graph Traversal – Path Exists
# Prompt:
# Given a dict representing a graph, write a function path_exists(graph, start, end) that returns True if a path exists from start to end.

# graph = {
#   "USD": ["EUR", "GBP"],
#   "EUR": ["JPY"],
#   "GBP": ["INR"]
# }
# Focus: BFS or DFS, avoiding cycles
from collections import deque

class Graph:
    def __init__(self):
        pass

    def path_exists(self, graph, start, end, visited=None):
        if visited is None:
            visited = set()
        if start == end:
            return True
        if start not in graph or start in visited:
            return False
        
        visited.add(start)
        
        for neighbor in graph[start]:
            if self.path_exists(graph, neighbor, end, visited):
                return True
        return False
    
    def path_exists_queue(self, graph, start, end):
        queue = deque([start])
        visited = set()

        while queue:
            curr = deque.popleft(queue)

            if curr == end:
                return True
            
            if curr in graph and curr not in visited:
                for neighbor in graph[curr]:
                    queue.append(neighbor)
            visited.add(curr)
        return False
    
    def get_all_paths(self, graph):
        paths = []

        for node in graph:
            path = self.find_paths(graph, node)
            paths.append(path)
        return paths
    
    def find_paths(self, graph, node, curr_path=None, visited=None):
        if curr_path is None:
            curr_path = []
        if visited is None:
            visited = set()
        
        curr_path.append(node)

        if node not in graph or node in visited:
            return curr_path
        
        visited.add(node)

        for neighbor in graph[node]:
            self.find_paths(graph, neighbor, curr_path, visited)

        return curr_path

# USD - EUR - JPY - USD - GBP - INR
# EUR - JPY - USD - EUR - GBP - INR
# GBP - INR
# BRL

graph = {
        "USD": ["EUR", "GBP"],
        "EUR": ["JPY", "USD"],
        "GBP": ["INR"],
        "BRL": [""]
        }

graph_class = Graph()
#print(graph_class.path_exists(graph, "EUR", "INR"))
#print(graph_class.path_exists_queue(graph, "EUR", "INR"))

#print(graph_class.get_all_paths(graph))

# Given a graph of currency conversions, 
# write a function find_conversion_path(from_currency, to_currency) 
# that returns a list of currencies representing the path (e.g., ["USD", "EUR", "JPY"])

# Bonus: Return the total conversion rate from start to end.

rates = {
    "USD": {"EUR": 0.9, "GBP": 0.75},
    "EUR": {"JPY": 130},
    "GBP": {"INR": 100}
}

def get_path(rates, current_currency, final_currency, path, visited, curr_rate=1):
    visited.add(current_currency)
    path.append(current_currency)

    if final_currency in current_currency:
        return (path, curr_rate)
    
    if current_currency not in rates:
        return

    for (currency, rate) in rates[current_currency].items():
        if currency not in visited:
            curr_path = get_path(rates, currency, final_currency, path[:], visited, curr_rate*rate)
            if curr_path: return curr_path

def find_conversion_path(rates, current_currency, final_currency):
    return get_path(rates=rates, current_currency=current_currency, final_currency=final_currency, path=[], visited=set())
    
        
print(find_conversion_path(rates=rates, current_currency="USD", final_currency="EUR")) # 0.9
print(find_conversion_path(rates=rates, current_currency="USD", final_currency="JPY")) # 117
print(find_conversion_path(rates=rates, current_currency="USD", final_currency="INR")) # 75
print(find_conversion_path(rates=rates, current_currency="USD", final_currency="BRL")) # None


