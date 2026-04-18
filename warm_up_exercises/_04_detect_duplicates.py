# 4. HashSet: Detect Duplicates in Stream
# Prompt:
# Write a function has_duplicate(nums: List[int]) -> bool
# Return True if the list contains any duplicates.

# Focus: Set usage, memory/time trade-offs

class Stream:
    def __init__(self):
        self.memo = set()
        self.storage = []
    
    def check_duplicates(self, new_num):
        duplicate = new_num in self.memo
        self.memo.add(new_num)
        self.storage.append(new_num)
        return duplicate
    
# import random
# stream = Stream()

# for i in range(100):
#     print(stream.check_duplicates(random.randint(1,100)))