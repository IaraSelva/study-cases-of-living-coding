import unittest
from _03_sliding_window import Solution

class Test(unittest.TestCase):
    def test_sliding_window(self):
        # Arrange
        solution = Solution()
        input_array = [1,3,-1,-3,5,3,6,7]
        window_size = 3
        expected_response = [3,3,5,5,6,7]

        # Act
        actual_response = solution.max_in_sliding_window(input_array, window_size)

        # Assert
        self.assertEqual(expected_response, actual_response)

if __name__ == '__main__':
    unittest.main()