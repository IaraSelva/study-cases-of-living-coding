class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.node = None
    
    # Inserir - primeiro, na função insert checar se o primeiro nó está vazio
    # Se sim, ele recebe o nó atual contendo o novo valor
    # Se não, a chamar a função recursiva que percorre toda a lista até achar o último nó
    def recursive_insert(self, node, new_node):
        if node.next is None:
            node.next = new_node
        else:
            if node.next:
                self.recursive_insert(node.next, new_node)
    
    def insert(self, value):
        new_node = Node(value)
        if self.node is None:
            self.node = new_node
            return self.node
        else: 
            return self.recursive_insert(self.node, new_node)
    
    # Printar - Checar se o primeiro nó não é vazio
    # Chamar a função recursiva passando o nó
    # A função printa depois chama ela mesma passando o next, enquanto existir next
    def recursive_print(self, node):
        print(node.value)
        if node.next:
            self.recursive_print(node.next)

    def print(self):
        if self.node is None:
            print(None)
            return
        else:
            self.recursive_print(self.node)

    # Inserir em uma posição específica
    def find_position_insert(self, node, cur_position, position, new_node):
        # Ex: 2 -> 3 -> 5 -> 7
        # inserir 4 na posição 2
        # o 3 passa a apontar para o 2
        # e o 2 deve apontar para o 5
        if cur_position == position-1:
            node.next, new_node.next = new_node, node.next
            return self.node
        if node.next:
            cur_position += 1
            self.find_position_insert(node.next, cur_position, position, new_node)

    def insert_at_position(self, position, value):
        new_node = Node(value)
        if self.node is None:
            return None
        # Ex: 2 -> 3 -> 5 -> 7
        # inserir 1 na posição 0
        # o next do novo nó aponta para o primeiro
        # e o novo nó toma o lugar do self.node (que representa o primeiro nó)
        if position == 0:
            new_node.next, self.node = self.node, new_node
        else: 
            cur_position = 0
            self.find_position_insert(self.node, cur_position, position, new_node)



linked_list = LinkedList()
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(5)
linked_list.insert(7)
linked_list.print()
print("\n__________________\n")
linked_list.insert_at_position(2, 4)
linked_list.print()
print("\n__________________\n")
linked_list.insert_at_position(0, 1)
linked_list.print()
print("\n__________________\n")
linked_list.insert_at_position(6, 8)
linked_list.print()
print("\n__________________\n")
linked_list.insert_at_position(5, 6)
linked_list.print()