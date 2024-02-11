import unittest
import requests
import json
import argparse


class MyFirstTestCase(unittest.TestCase):
    def test_healthcheck_fn(self):
        url = f"{args.base_url}/healthcheck"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_train_fn(self):
        url = f"{args.base_url}/api/mindsdb/classifier/train"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "name_of_model": "regression_model",
            "db_credentials": {
                "db_rename": "new_db",
                "engine": "postgres",
                "user": "demo_user",
                "password": "demo_password",
                "host": "3.220.66.106",
                "port": 5432,
                "db_name": "demo"
            },
            "mindsdb_credentials": {
                "subscription": "local"
            },
            "training_set_schema": "demo_data",
            "training_set_tableName": "home_rentals",
            "input_columns_names": "*",
            "output_column_names": "rental_price",
            "project_name": "new_project"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response.json()["status"], "success")


class MySecondTestCase(unittest.TestCase):
    def test_models_fn1(self):
        url = f"{args.base_url}/api/mindsdb/classifier/models"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "mindsdb_credentials": {
                "subscription": "local"
            },
            "project_name": "new_project"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.assertEqual(response.json()["status"], "success")

    def test_models_fn2(self):
        url = f"{args.base_url}/api/mindsdb/classifier/models"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "mindsdb_credentials": {
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
    parser = argparse.ArgumentParser(description='Run tests with custom base URL')
    parser.add_argument('--base_url', type=str, default="http://localhost:8080", help='Base URL for the API')
    args = parser.parse_args()
    runner = unittest.TextTestRunner()
    runner.run(suite())
