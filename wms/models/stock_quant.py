# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class StockQuantSchema:
    stock_quant_req = {
        'products': fields.String(required=True, description='List sku'),
        'branches': fields.String(required=False, description='Branches'),
        'warehouses': fields.String(required=False, description='Warehouses code'),
        'locations': fields.String(required=False, description='Locations'),
        'regions': fields.Integer(required=False, description='Regions'),
    }

    stock_quant_item = {
        # 'sku': fields.String(required=True, description='product sku'),
        'location': fields.String(required=False, description='Branch'),
        'warehouse': fields.String(required=False, description='Warehouse code'),
        'reserved': fields.Float(required=False, description='Stock held quantity'),
        'incoming': fields.Integer(required=False, description='Quantity about to enter stock'),
        'storeCode': fields.String(required=False, description='Asia region type'),
        'outgoing': fields.Integer(required=False, description='Stock outgoing quantity'),
        'available': fields.Float(required=False,
                                  description='Available quantity = Actual inventory number - stock held = onHand- reserved',
                                  ),
        'forecast': fields.Float(required=False, description='No description'),
        'onHand': fields.Float(required=False, description='Actual quantity in stock'),
        'productBizType': fields.String(required=False, description='Type of product business'),
    }
    # Remove some fields for stock_quant_item_min
    stock_quant_item_min = stock_quant_item.copy()
    stock_quant_item_min.pop('incoming')
    stock_quant_item_min.pop('forecast')
    stock_quant_item_min.pop('outgoing')

