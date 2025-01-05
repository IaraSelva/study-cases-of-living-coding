import heapq

nums = []

heapq.heapify(nums)

heapq.heappush(nums, (9, 1))
heapq.heappush(nums, (3, 2))
heapq.heappush(nums, (8, 1))
heapq.heappush(nums, (7, 2))
min = heapq.heappop(nums)
min = heapq.heappop(nums)

#print(nums)
#print(f"min value = {min}")


def build_graph(times):
    graph = {}
    for node, neighbor, distance in times:
        if node not in graph:
            graph[node] = []
        if neighbor not in graph:
            graph[neighbor] = []
        graph[node].append((distance, neighbor))
        graph[neighbor].append((distance, node))
    return graph

def min_path(source, target, times):
    graph = build_graph(times)
    queue = [(0, source)]
    heapq.heapify(queue)
    visited = set()

    while queue: # [(1,1)]
        min_path, node = heapq.heappop(queue) # 0 
        visited.add(node)
        if node == target: 
            return min_path
        
        for dist, neighbor in graph[node]: # 1 -- 1
            if neighbor not in visited:
                heapq.heappush(queue, (dist + min_path, neighbor))
    
    return -1
    
def networkDelayTime(times, source, target):
    return min_path(source, target, times)

times = [[2,1,1],[2,3,1],[3,4,1]]
target = 4
source = 2
print(build_graph(times))
print(networkDelayTime(times, source, target))

'''
2 --1-- 1
:
1
:
3 --1-- 4

1 --1-- 3
:       :
4       2
:       :
2 --3-- 4 --5-- 5 --2-- 7
                :
                3
                :
                6
'''
# node, neighbor, distance
times = [[1,3,1],[1,2,4],[2,4,3],[3,4,2],[4,5,5],[5,6,3],[5,7,2]]
source = 1
target = 7
print(build_graph(times))
print(networkDelayTime(times, source, target))

# node, neighbor, distance
times = [['A','B',1],['B','C',2],['A','D',7],['C','D',1],['D','E',2],['D','F',2],['F','E',3],['E','G',4],['E','H',5],['G','H',6]]
source = 'A'
target = 'E'
print(build_graph(times))
print(networkDelayTime(times, source, target))