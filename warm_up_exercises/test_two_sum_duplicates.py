import unittest
from _01_two_sum_duplicates import Solution
class TestSolution(unittest.TestCase):
    def test_case_solution(self):
        # Arrange
        solution = Solution()
        input = [([2, 3, 4, 3], 6), ([3, 3, 3, 3], 6)]
        expected = [[(0,2), (1,3)], [(0,1), (0,2), (1,2), (0,3), (1,3), (2,3)]]

        # Act
        for i, (nums, target) in enumerate(input):
            result = solution.two_sum_duplicate(nums, target)

            # Assert
            self.assertEqual(result, expected[i])
    
if __name__ == '__main__':
    unittest.main()