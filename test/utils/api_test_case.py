import unittest
import json

class APITestCase(unittest.TestCase):
    accounts = None

    @classmethod
    def setUpClass(cls):
        with open('./travis-ci/accounts.json') as json_data:
            cls.accounts = json.load(json_data)
            