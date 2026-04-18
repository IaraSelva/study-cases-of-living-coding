import unittest
from _04_detect_duplicates import Stream

class Test(unittest.TestCase):
    def test_detect_duplicates(self):
        # Arrange
        stream = Stream()
        numbers = [1,2,3,4,5,6,7,8,9]

        # Act
        for num in numbers:
            response = stream.check_duplicates(num)

            # Assert
            self.assertEqual(response, False)

        for num in numbers:
            response = stream.check_duplicates(num)

            # Assert
            self.assertEqual(response, True)

    def test_random_duplicates(self):
        # Arrange
        stream = Stream()
        numbers = [1,2,3,2,4,1]
        expected_output = [False, False, False, True, False, True]

        # Act
        for i, num in enumerate(numbers):
            response = stream.check_duplicates(num)

            # Assert
            self.assertEqual(response, expected_output[i])
