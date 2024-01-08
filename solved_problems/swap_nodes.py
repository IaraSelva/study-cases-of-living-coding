def swapNodes(indexes, queries):
    new_tree = Tree(indexes)
    result = []

    for query in queries:
        new_tree.swap(query)
        swaped = new_tree.printTree([])
        result.append(swaped)
    
    return result


class Node:
    def __init__(self, value, depth):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth

class Tree:
    def __init__(self, indexes):
        self.indexes = indexes
        self.root = self.insert(1,1)

    def insert(self, value, depth):
        new_node = Node(value, depth)

        left_node_value = self.indexes[value-1][0]
        right_node_value = self.indexes[value-1][1]
        
        new_node.left = None if left_node_value == -1 else self.insert(left_node_value, depth +1)
        new_node.right = None if right_node_value == -1 else self.insert(right_node_value, depth +1)

        return new_node
    
    def printTree(self, arr, node = None):
        if node is None: node = self.root

        if node.left is not None: self.printTree(arr, node.left)
        arr.append(node.value)
        if node.right is not None: self.printTree(arr, node.right)

        return arr
    
    def swap(self, k, node = None):
        if node is None: node = self.root

        if node.depth % k == 0:
            node.left, node.right = node.right, node.left
        
        if node.left is not None: self.swap(k, node.left)
        if node.right is not None: self.swap(k, node.right)

print(swapNodes([[2, 3], [-1, -1], [-1, -1]], [1, 1]))
print(swapNodes([[2, 3],[4, 5],[6, -1],[-1, 7],[8, 9],[10, 11],[12, 13],[-1, 14],[-1, -1],[15, -1],[16, 17],[-1, -1],[-1, -1],[-1, -1],[-1, -1],[-1, -1],[-1, -1]],[2,3]))