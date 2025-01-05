class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"val = {self.val}, right: {self.right}, left: {self.left}"

class Tree:
    def __init__(self):
        self.root = None
    
    def __repr__(self) -> str:
        return f"{self.root}"

    def recursiveInsert(self, curr_node, new_node):
        if curr_node is None:
            curr_node = new_node
            return curr_node
        
        if new_node.val < curr_node.val:
            curr_node.left = self.recursiveInsert(curr_node.left, new_node)
        else:
            curr_node.right = self.recursiveInsert(curr_node.right, new_node)
        return curr_node
    
    def insert(self, val):
        new_node = Node(val)
        
        if self.root is None:
            self.root = new_node
            return
        
        return self.recursiveInsert(self.root, new_node)
    
    def print(self):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    
tree = Tree()
tree.insert(100)
tree.insert(120)
tree.insert(80)
tree.insert(50)
tree.insert(90)
tree.insert(110)
tree.insert(140)
tree.insert(30)
tree.insert(60)
tree.insert(85)
tree.insert(95)
tree.insert(115)
tree.insert(150)
tree.insert(108)

tree.print()        