# 3. Sliding Window Max
# Prompt:
# Write a function max_in_sliding_window(nums: List[int], k: int) -> List[int]
# Return a list of the max value in each window of size k.
# Example: max_in_sliding_window([1,3,-1,-3,5,3,6,7], 3) => [3,3,5,5,6,7]

# Focus: Queue/Deque logic, window control

# Approach: 
# a sorted queue (cache) containing the numbers within the window in descendent order
# for each iteration, a number is pushed
# remove only if the cache is full (the size of the window)
# remove from index* - a list of index indicating the index of the cache
# insert using binary search to keep it in descendent order
# to add the max, check if the largest number is still within the window

from collections import deque
import itertools

class Solution:
    def __init__(self):
        pass

    def max_in_sliding_window(self, nums, window_size):
        max_values = []
        cache = []
        original_index_to_cache = []

        for i, num in enumerate(nums):
            print(f"cache = {cache}")
            if len(cache) == window_size:
                max_values.append(cache[0])
            if len(cache) > window_size:
                # remove
                print("remove")
                index_to_remove = original_index_to_cache.pop(0)
                print(f"index to remove = {index_to_remove}")
                cache.pop(index_to_remove)
            else:
                # insert
                print("insert")
                index_to_insert = self.binary_search_index(cache, num)
                cache.insert(index_to_insert, num)
                original_index_to_cache.append(i + index_to_insert)
                print(f"original_index_to_cache {original_index_to_cache}")
            

        return max_values

    def binary_search_index(self, window, num_to_insert, start_index=0):
        if len(window) == 0: return 0

        mid = len(window)//2

        if len(window) == 1:
            if window[mid] > num_to_insert:
                return start_index + mid + 1
            else:
                return start_index + mid
        
        if window[mid] > num_to_insert:
            deque_slice = deque(itertools.islice(window, mid, len(window)))
            return self.binary_search_index(deque_slice, num_to_insert, start_index+mid)
        elif window[mid] < num_to_insert:
            deque_slice = deque(itertools.islice(window, 0, mid))
            return self.binary_search_index(deque_slice, num_to_insert, start_index)


test = Solution()
print(test.max_in_sliding_window([1,3,-1,-3,5,3,6,7], 3))
            


