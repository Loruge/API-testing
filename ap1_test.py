import unittest
from ap1 import *


class TestApiProcess(unittest.TestCase):

    def test_api_url_correct(self):
        self.assertEqual(testin.url, 'www.auth_api.info/admin/company/208/branches', 'Not exist or wrong URL')

    def test_api_method_post(self):
        self.assertEqual(testin.method, 'Post', 'Wrong method')

    def test_api_payload_correct(self):
        self.assertEqual(testin.payload, 'company_name, company_number, company_internal_id', 'Payload incorrect')

    def test_api_url_incorrect(self):
        self.assertNotEqual(testin.url, 'www.auth_api.info/admin/company/208/branche0', 'Url correct')

    def test_api_method_not_post(self):
        self.assertNotEqual(testin.method, 'Get', 'Correct method')

    def test_api_payload_incorrect(self):
        self.assertNotEqual(testin.payload, 'company_name, company_number, company_internal', 'Payload correct')

    def test_api_info_response_correct(self):
        self.assertEqual(testin.response, {'date': '20.02.2012', 'id': 77, 'info': 'information', 'time': '11:27'},
                         'wrong')

    def test_api_info_response_incorrect(self):
        self.assertNotEqual(testin.response, {'date': '20.02.2012', 'id': 77, 'info': 'information', 'time': '11:28'},
                            'Response is correct')

    def test_api_all(self):
        self.assertEqual(testin.url, 'www.auth_api.info/admin/company/208/branches', 'wrong')
        self.assertEqual(testin.method, 'Post', 'wrong')
        self.assertEqual(testin.payload, 'company_name, company_number, company_internal_id', 'wrong')
        self.assertEqual(testin.response, {'date': '20.02.2012', 'id': 77, 'info': 'information', 'time': '11:27'},
                         'wrong')
