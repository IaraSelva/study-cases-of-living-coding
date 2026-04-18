import unittest
from fastapi.testclient import TestClient
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        # Arrange
        expected_status_code = 200
        expected_response = {"status": "ok"}

        # Act
        response = self.client.get("/")
        
        # Asserts
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_response)

    def test_has_path_true(self):
        # Arrange
        input_data = {
            "edges": [
                ["USD", "EUR"],
                ["USD", "GBP"],
                ["EUR", "JPY"],
                ["EUR", "USD"],
                ["GBP", "INR"],
                ["BRL", ""]
            ]
        }
        source = "USD"
        target = "INR"
        expected_status_code = 200
        expected_response = {"pathExists": True}

        # Act
        response = self.client.post(f"/has-path?source={source}&target={target}", json=input_data)

        # Asserts
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_response)

    def test_has_path_false(self):
        # Arrange
        input_data = {
            "edges": [
                ["USD", "EUR"],
                ["USD", "GBP"],
                ["EUR", "JPY"],
                ["EUR", "USD"],
                ["GBP", "INR"],
                ["BRL", ""]
            ]
        }
        source = "BRL"
        target = "INR"
        expected_status_code = 200
        expected_response = {"pathExists": False}

        # Act
        response = self.client.post(f"/has-path?source={source}&target={target}", json=input_data)

        # Asserts
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.json(), expected_response)

if __name__ == "__main__":
    unittest.main()