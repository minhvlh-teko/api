# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class StockQuantSchema:
    stock_quant_req = {
        'products': fields.String(required=True, description='List sku'),
        'branches': fields.String(required=False, description='Chi nhánh'),
        'warehouses': fields.String(required=False, description='Mã Kho'),
        'locations': fields.String(required=False, description='Địa điểm'),
        'regions': fields.Integer(required=False, description='Vùng / miền'),
    }

    stock_quant_item = {
        # 'sku': fields.String(required=True, description='product sku'),
        'location': fields.String(required=False, description='Chi nhánh'),
        'warehouse': fields.String(required=False, description='Mã Kho'),
        'reserved': fields.Float(required=False, description='Số lượng đã giữ'),
        'incoming': fields.Integer(required=False, description='Số lượng sắp nhập kho'),
        'storeCode': fields.String(required=False, description='loại khu vực Asia'),
        'outgoing': fields.Integer(required=False, description='Số lượng sắp xuất kho'),
        'available': fields.Float(required=False,
                                  description='Số lượng tồn kho thực tế - số đã giữ hàng = on_hand- reserved',
                                  ),
        'forecast': fields.Float(required=False, description='No description'),
        'onHand': fields.Float(required=False, description='Số lượng thực tế đang có trong kho'),
        'productBizType': fields.String(required=False, description='Loại hình kinh doanh sản phẩm'),
    }
    # Remove some fields for stock_quant_item_min
    stock_quant_item_min = stock_quant_item.copy()
    stock_quant_item_min.pop('incoming')
    stock_quant_item_min.pop('forecast')
    stock_quant_item_min.pop('outgoing')

