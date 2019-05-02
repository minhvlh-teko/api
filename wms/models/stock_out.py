# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class StockOutSchema:
    stock_out_request_req = {
        'requestCode': fields.String(required=True, description='Request code'),
        'requestType': fields.Integer(required=True, description='Request type'),
        'orderID': fields.String(required=True, description='Order code (if in other export type, orderID = 0)'),
        'createdAt': fields.DateTime(required=True, description='Request time'),
    }

    stock_out_confirm_req = {
        'requestCode': fields.String(required=True, description='Request code'),
        'staffId': fields.Integer(required=True, description='Staff ID'),
        'orderID': fields.String(required=True, description='Order ID'),
        'createdAt': fields.DateTime(required=True, description='Confirmation time'),
    }
