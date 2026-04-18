# 6. Sorting & Binary Search – Price Check
# Prompt:
# Given a sorted list of prices and a target price, return the index where the target exists, or where it should be inserted.

# Practice: bisect module, custom binary search

class Solution:
    def __init__(self):
        pass

    def binary_search(self, nums, target, start_index=0):
        mid = len(nums)//2

        if nums[mid] == target:
            return mid + start_index
        if len(nums) == 1:
            if nums[mid] > target:
                return mid + start_index
            else:
                return mid + start_index + 1
        if nums[mid] > target:
            return self.binary_search(nums[:mid], target, start_index)
        else:
            return self.binary_search(nums[mid:], target, start_index + mid)
        

my_class = Solution()
print(my_class.binary_search([1,3,5,7,9], 0))
