# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'MinhVlh'
_logger = logging.getLogger('api')


class TekoBizTypeLocationDetailSchema:
    stock_quant_req = {
        'warehouses': fields.String(required=False, description='Warehouses code'),
        # 'location_code': fields.String(required=False, description='location code'),

    }

    teko_biz_type_location_detail_res = {
        'location_code': fields.String(required=False, description='Branch'),
        'warehouse_code': fields.String(required=False, description='Warehouse code'),
        'product_biz_type_code': fields.String(required=False, description='Type of product business'),
    }


