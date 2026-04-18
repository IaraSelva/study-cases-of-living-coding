#1. Array & HashMap: Two Sum with Duplicates
#Prompt:
#Given a list of integers nums and an integer target, return all pairs of indices where the numbers add up to the target.
#Example: two_sum([2, 3, 4, 3], 6) should return [(0,2), (1,3)]

#Focus: Dict usage, iteration, duplicates

#Approach:
# a dict to store the complement of each number as key and the index as value
# a list of tuples of the indexes to be returned
# iterate throught the list and check if the number exists in compl dict
    # if there's, add it value and the index as a tuple to the response array
# calculate the compl and store it into the dict

class Solution:
    def __init__(self):
        pass

    def two_sum_duplicate(self, numbers, target):
        compl_index = {}
        indexes = []

        for i, num in enumerate(numbers): # O (n)            
            if num in compl_index:
                for index in compl_index[num]:
                    indexes.append((index, i)) # O (j) if all the numbers are equal is gonna be nˆ2 ?
            compl = target - num
            if compl in compl_index:
                compl_index[compl].append(i)
            else:
                compl_index[compl] = [i]

        return indexes
