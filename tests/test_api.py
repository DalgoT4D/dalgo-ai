import unittest
import requests
import json


class MyFirstTestCase(unittest.TestCase):
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
            "output_column_names": "rental_price",
            "project_name": "example_db"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response.json()["status"], "success")


class MySecondTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8080"

    def test_models_fn1(self):
        url = f"{self.base_url}/api/mindsdb/classifier/models"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "db_credentials": {
                "subscription": "local"
            },
            "project_name": "example_db"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response.json()["status"], "success")

    def test_models_fn2(self):
        url = f"{self.base_url}/api/mindsdb/classifier/models"
        headers = {'Content-Type': 'application/json'}
        payload ={
            "db_credentials": {
                "subscription": "local"
            }
        }
        response2 = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response2.json()["status"], "success")


def suite():
    suit = unittest.TestSuite()
    suit.addTest(MyFirstTestCase('test_healthcheck_fn'))
    suit.addTest(MyFirstTestCase('test_train_fn'))
    suit.addTest(MySecondTestCase('test_models_fn1'))
    suit.addTest(MySecondTestCase('test_models_fn2'))
    return suit


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
