import unittest
from warm_up_exercises._06_binary_search import Solution

class Test(unittest.TestCase):
    
    def test_binary_search(self):
        # Arrange
        solution_class = Solution()
        test_cases = [([1,3,5,7,9], 0), ([1,6,8], 9), ([2,3,4,5,7,8], 6), ([1,2,3,4,5,6], 3), ([3,4,5,7,9], 9)]
        expected_output = [0,3,4,2,4]

        # Act
        for i, (array, target) in enumerate(test_cases):
            response = solution_class.binary_search(array, target)
        # Asserts
            self.assertEqual(response, expected_output[i])
