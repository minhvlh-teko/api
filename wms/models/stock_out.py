# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class StockOutSchema:
    stock_out_request_req = {
        'requestCode': fields.String(required=True, description='Mã phiếu xuất kho'),
        'requestType': fields.Integer(required=True, description='Loại xuất'),
        'orderID': fields.String(required=True, description='Mã đơn hàng (nếu thuộc loại xuất khác thì orderID = 0)'),
        'createdAt': fields.DateTime(required=True, description='Thời gian yêu cầu'),
    }

    stock_out_confirm_req = {
        'requestCode': fields.String(required=True, description='Mã phiếu xuất kho'),
        'staffId': fields.Integer(required=True, description='Mã nhân viên nhận hàng'),
        'orderID': fields.String(required=True, description='mã đơn hàng (nếu thuộc loại xuất khác thì orderID = 0)'),
        'createdAt': fields.DateTime(required=True, description='Thời gian xác nhận'),
    }
