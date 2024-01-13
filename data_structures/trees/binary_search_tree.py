class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 1
    
    def height(self):
        if self.left is None and self.right is None: return 0

        right_height = self.right.height() if self.right is not None else 0
        left_height = self.left.height() if self.left is not None else 0

        if right_height > left_height:
            return right_height + 1
        else:
            return left_height + 1


class Tree:
    def __init__(self):
        self.root = None

    def recursiveInsert(self, node, newNode):
        if node.value > newNode.value:
            if node.left is None:
                newNode.depth = node.depth +1
                node.left = newNode
                return newNode
            self.recursiveInsert(node.left, newNode)
        else:
            if node.right is None:
                newNode.depth = node.depth +1
                node.right = newNode
                return newNode
            self.recursiveInsert(node.right, newNode)

    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None: 
            self.root = new_node
            return new_node
        
        return self.recursiveInsert(self.root, new_node)
    
    def printTree(self, node = None, position = None):
        if self.root == None: 
            print(None)
            return None
        if node is None: 
            node = self.root
            position = "root"

        print(position, end=": ")
        print(node.value)
        
        if node.left is not None: 
            if node.left.depth > node.depth:
                position = f"leafs of {node.value}"
            self.printTree(node.left, position= position + " left")
        if node.right is not None: 
            if node.right.depth > node.depth:
                position = f"leafs of {node.value}"
            self.printTree(node.right, position= position + " right")
    
    def height(self):
        if self.root is None: return 0
        return self.root.height()
    
    def depth(self, node = None):
        if self.root == None: return 0
        if node == None: node = self.root

        depth_right = node.depth if node.right is None else self.depth(node.right)
        depth_left = node.depth if node.left is None else self.depth(node.left)

        if depth_right > depth_left:
            return depth_right
        return depth_left
    
    def findMin(self, node = None):
        if self.root is None: return None
        if node == None: node = self.root

        return node.value if node.left is None else self.findMin(node.left)
    
    def findMax(self, node = None):
        if self.root is None: return None
        if node == None: node = self.root

        return node.value if node.right is None else self.findMax(node.right)

    def swap(self, node = None):
        if self.root is None: return None
        if node is None: node = self.root

        if node.left: self.swap(node.left)
        if node.right: self.swap(node.right)

        node.left, node.right = node.right, node.left

       

tree = Tree()
print("empty tree")
tree.printTree()
print(f"height: {tree.height()}")
print(f"depth: {tree.depth()}")
print(f"min: {tree.findMin()}")
print(f"max: {tree.findMax()}")
tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(9)
tree.insert(10)
print("tree after insertion")
tree.printTree()
print(f"height: {tree.height()}")
print(f"depth: {tree.depth()}")
print(f"min: {tree.findMin()}")
print(f"max: {tree.findMax()}")
tree.swap()
print("tree after swap")
tree.printTree()