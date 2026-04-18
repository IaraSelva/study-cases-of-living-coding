import unittest
from _05_path_exists import Graph

class Test(unittest.TestCase):

    def test_has_path(self):
        # Arrange
        graph_class = Graph()
        given_graph = {
                    "USD": ["EUR", "GBP"],
                    "EUR": ["JPY", "USD"],
                    "GBP": ["INR"],
                    "BRL": []
                    }
        inputs = [("USD", "EUR"), ("USD", "GBP"), ("GBP", "JPY"), ("GBP", "INR"), ("EUR", "JPY"), ("INR", "GBP"), ("USD", "INR"), ("EUR", "INR"), ("BRL", "USD"), ("XXX", "YYY")]
        outputs = [True, True, False, True, True, False, True, True, False, False]

        # Act
        for i, (source, target) in enumerate(inputs):
            response = graph_class.path_exists(given_graph, source, target)

            # Assert
            self.assertEqual(response, outputs[i])

    def test_has_path_queue(self):
            # Arrange
            graph_class = Graph()
            given_graph = {
                        "USD": ["EUR", "GBP"],
                        "EUR": ["JPY", "USD"],
                        "GBP": ["INR"],
                        "BRL": [""]
                        }
            inputs = [("USD", "EUR"), ("USD", "GBP"), ("GBP", "JPY"), ("GBP", "INR"), ("EUR", "JPY"), ("INR", "GBP"), ("USD", "INR"), ("EUR", "INR"), ("BRL", "USD"), ("XXX", "YYY")]
            outputs = [True, True, False, True, True, False, True, True, False, False]

            # Act
            for i, (source, target) in enumerate(inputs):
                response = graph_class.path_exists_queue(given_graph, source, target)

                # Assert
                self.assertEqual(response, outputs[i])

    def test_get_all_paths(self):
        # Arrange
        graph_class = Graph()
        input_graph  = {
                        "USD": ["EUR", "GBP"],
                        "EUR": ["JPY", "USD"],
                        "GBP": ["INR"],
                        "BRL": [""]     
                    }
        expected_output = [['USD', 'EUR', 'JPY', 'USD', 'GBP', 'INR'], ['EUR', 'JPY', 'USD', 'EUR', 'GBP', 'INR'], ['GBP', 'INR'], ['BRL', '']]

        # Act
        response = graph_class.get_all_paths(input_graph)

        # Assert
        self.assertEqual(response, expected_output)

if __name__ == '__main__':
    unittest.main()