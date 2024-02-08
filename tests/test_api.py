import unittest
import requests
import json


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8080"

    def test_healthcheck_fn(self):
        url = f"{self.base_url}/healthcheck"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_train_fn(self):
        url = f"{self.base_url}/api/mindsdb/classifier/train"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "name_of_model": "test_regression_model",
            "db_credentials": {
                "db_name": "example_db",
                "subscription": "local"
            },
            "training_set_schema": "demo_data",
            "training_set_tableName": "home_rentals",
            "input_columns_names": "*",
            "output_column_names": "rentals_price"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response.json()["status"], "success")


if __name__ == '__main__':
    unittest.main()
