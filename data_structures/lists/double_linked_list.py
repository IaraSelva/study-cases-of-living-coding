class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
class LinkedList:
    def __init__(self):
        self.root = None

    def recursiveInsert(self, current_node, new_node):
        if current_node.next is None:
            current_node.next = new_node
            new_node.previous = current_node
        else:
            self.recursiveInsert(current_node.next, new_node)
        return new_node

    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None: self.root = new_node
        else: 
            self.recursiveInsert(self.root, new_node)
        return new_node
    
    def print_list(self, node = None):
        if self.root is None: return None
        if node is None: node = self.root

        print(node.value, end=" ")
        if node.next: self.print_list(node.next)
        else: print("\n")
    
    def find_position_insert(self, node, new_node):
        # 1 3 4 
        # iserir 2
        # o node(1).next passa a ser node(2)
        # node(2).prev = node(1)
        # node(2).next precisa apontar pro antigo node.next = node(3)
        if node.next is None:
            node.next, new_node.previous = new_node, node
        elif node.next.value > new_node.value:
            new_node.next = node.next # node(2) -next-> node(3)
            node.next.previous = new_node # node(3) -prev-> node(2)
            node.next, new_node.previous = new_node, node # node(1) -next-> node(2) -prev-> node(1)
        elif node.next:
            self.find_position_insert(node.next, new_node)    
    
    def insert_sort(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        if self.root.value > value:
            new_node.next, self.root.previous = self.root, new_node
            self.root = new_node
        else:
            self.find_position_insert(self.root, new_node)
    
    # 0 1 2 3 4 5 7 8 8 15
    def reverse(self, node):
        node.previous, node.next = node.next, node.previous #node(0) -prev-> node(1) -next-> node(0)
        if node.previous:
            self.reverse(node.previous)
        else: self.root = node # quando chegamos ao último, root agora é esse último node

    def reverse_list(self):
        if self.root is None:
            return None
        self.reverse(self.root)


new_list = LinkedList()
new_list.insert(1)
new_list.insert(3)
new_list.insert(4)
new_list.print_list()
new_list.insert_sort(2)
new_list.print_list()
new_list.insert_sort(0)
new_list.print_list()
new_list.insert_sort(5)
new_list.print_list()
new_list.insert_sort(15)
new_list.print_list()
new_list.insert_sort(8)
new_list.print_list()
new_list.insert_sort(8)
new_list.print_list()
new_list.insert_sort(7)
new_list.print_list()
new_list.reverse_list()
new_list.print_list()