'''
A security linked list is a linked list that have one moreattribute which is hash_value
The hash value is formed by the value of the curr node + hash value of the next node

There's a function 
hash(str) -> int
That given an string is gonna return a hash int 

The nodes are inserted at the head of the list, not at the tail

SecurityLinkedList:
    value
    next
    hash_value

Create two functions:

add_value -> add a new node
is_valid -> check if the security linked list is valid
'''