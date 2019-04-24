# coding=utf-8
import json
import logging

# from .. import models as m
from . import APITestCase

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


class StockQuantApiTestCase(APITestCase):
    def url(self):
        return '/api/v2/stockQuants/'

    def method(self):
        return 'GET'

    def test_get_stock_quants_when_send_odoo_success_then_return_stock_quants_response_with_data(self):
        test_cases = [
            {
                'url': '/api/v2/stockQuants/?products=18120233',
                'skus': 1,
                'first_sku': 18120233,
                'first_sku_item_length_greater_than': 1
            },
            {
                'url': '/api/v2/stockQuants/?products=1200109&products=18120233',
                'skus': 2,
                'first_sku': 1200109,
                'first_sku_item_length_greater_than': 3
            },

        ]
        for item in test_cases:
            rv = self.send_request(url=item['url'])
            self.assertEqual(200, rv.status_code)
            res_data = json.loads(rv.data)['data']
            # number items should be greater than 0
            self.assertGreaterEqual(res_data, item['skus'])
            self.assertEqual(res_data[0]['sku'], item['first_sku'])
            self.assertGreaterEqual(res_data[0]['items'], item['first_sku_item_length_greater_than'])
            if item['first_sku_item_length']:
                self.assertIsNot(res_data[0]['items'][0]['warehouse'], '', 'Warehouse should not be empty')


    def test_get_stock_quants_when_invalid_query_params_then_return_400_code(self):
        test_cases = [
            {
                'url': '/api/v2/stockQuants/',
            },
            {
                'url': '/api/v2/stockQuants/?products=18120233,1200109',
            },
        ]

        for item in test_cases:
            rv = self.send_request(url=item['url'])
            self.assertEqual(400, rv.status_code)
