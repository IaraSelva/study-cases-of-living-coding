# 2. Queue with Python Lists (Rate Limiter Base)
# Prompt:
# Implement a class MyQueue with:
# enqueue(x)
# dequeue()
# size()

# Practice simulating queue logic using collections.deque or lists
from collections import deque
class Queue:
    def __init__(self):
        self.queue = []
        #self.queue = deque()
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0) # FIFO
        else:
            return None
    
    def remove(self, element_to_remove):
        for i, element in enumerate(self.queue):
            if element == element_to_remove:
                return self.queue.pop(i)
        return "Element not found"
    
    def size(self):
        return len(self.queue)

    def show(self):
        print(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(1)
queue.show()
print(queue.size())
queue.dequeue()
queue.show()
print(queue.remove(5))
queue.show()
print(queue.remove(8))
queue.show()

    


    