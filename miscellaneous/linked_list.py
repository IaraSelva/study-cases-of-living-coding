class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        return f"val = {self.val}, next: {self.next}"

class LinkedList:
    def __init__(self) -> None:
        self.root = None
    
    def __repr__(self) -> str:
        return f"{self.root}"

    def recursiveInsert(self, new_node, node):
        if node.next is None:
            node.next = new_node
            return self.root
        self.recursiveInsert(new_node, node.next)
    
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return self.root
        return self.recursiveInsert(new_node, self.root)
    
    def print(self, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print(self.root)
            return
        
        print(node.val)
        if node.next is None:
            return
        self.print(node.next)
    
    def contains(self, num, node=None):
        if self.root is None:
            return None
        if node is None:
            node = self.root
        
        if node.val == num:
            return True
        if node.next is None:
            return False
        return self.contains(num, node.next)

    def sum(self, sum=0, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            return None
        
        if node.next is None:
            return node.val + sum
        
        return node.val + self.sum(sum, node.next)
    
    def recursiveReverse(self, prev, curr):
        if curr is None:
            self.root = prev
            return self.root
        
        next = curr.next
        curr.next = prev

        prev = curr

        return self.recursiveReverse(prev, next)

    
    def reverse(self):
        if self.root is None:
            return None
        
        return self.recursiveReverse(None, self.root)
    
    def loopReverse(self):
        if self.root is None:
            return None
        
        curr = self.root
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.root = prev
        return self.root
        
    
    def zipperLists(self, list2):
        tail = self.root

        curr1 = self.root.next
        curr2 = list2.root

        count = 0
        while curr1 and curr2:
            if count % 2 == 0:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            count += 1
            tail = tail.next
        
        if curr1 is None:
            tail.next = curr2
        if curr2 is None:
            tail.next = curr1
        return self.root
    
    def mergeLists(self, list2):
        head = self.root if self.root.val < list2.root.val else list2.root
        tail = head
        curr1 = self.root
        curr2 = list2.root

        while curr1 and curr2:
            if curr1.val < curr2.val:
                next = curr1.next
                tail.next = curr1
                curr1 = next
            else:
                next = curr2.next
                tail.next = curr2
                curr2 = next
            tail = tail.next

        if curr1 is None:
            tail.next = curr2
        if curr2 is None:
            tail.next = curr1

        return head
    
    def compareMerge(self, nodeA, nodeB):
        if nodeA is None: return nodeB
        if nodeB is None: return nodeA

        if nodeA.val < nodeB.val:
            nodeA.next = self.compareMerge(nodeA.next, nodeB)
            return nodeA
        else:
            nodeB.next = self.compareMerge(nodeB.next, nodeA)
            return nodeB
    
    def mergeRecursively(self, list2):
        """if self.root is None:
            return list2.root
        if list2 is None:
            return self.root"""
        
        return self.compareMerge(self.root, list2.root)
          
    
'''
list = LinkedList()
list.insert(2)
list.insert(7)
list.insert(3)
list.insert(0)
list.insert(9)
list.print()
print(list.contains(9))
print(list.contains(10))
print("_________________")
print(list.sum())
print("_________________")
print(list.reverse())
list.print()
print("_________________")
print(list.loopReverse())
list.print()
print("_________________")
'''
list1 = LinkedList()
list1.insert(2)
list1.insert(7)
list2 = LinkedList()
list2.insert(2)
list2.insert(3)
list2.insert(4)
#print(list1.zipperLists(list2))
#list1.print()
#print("_________________")
#list2.print()
#print("_________________")
#print(list1.mergeLists(list2))
print(list1.mergeRecursively(list2))
list1.print()
print("_________________")
list2.print()
print("_________________")
