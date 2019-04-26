# coding=utf-8

import logging

from flask_restplus import fields, Model

__author__ = 'Huu'
_logger = logging.getLogger('api')


class EtonApiSchema:
    eton_product = Model('eton_product', {
        'sku': fields.String(required=True, description='Mã sản phẩm'),
        'qty': fields.Integer(required=True, description='Số lượng'),
        'serials': fields.List(fields.String, required=True, description='Danh sách serial')
    })

    eton_po_req = Model('eton_po_req', {
        'items': fields.Nested(eton_product, required=True, description='Danh sách thông tin sản phẩm cần xử lý')
    })

    eton_so_req = eton_po_req.clone('eton_so_req', {
        'eventType': fields.String(
            description='event type value MUST be: `picked`, `packed`, `delivered`, `returned`',
            enum=['picked', 'packed', 'delivered', 'returned']
        )
    })

    eton_so_returned_req = eton_so_req.clone('eton_so_req', {
        'type': fields.String(
            description='Loại return'
        )
    })

    eton_success_res = Model('eton_success_res', {
        'code': fields.Integer(example=0),
        'message': fields.String()
    })

    eton_fail_res = eton_success_res.clone('eton_fail_res', {
        'code': fields.Integer(example=1)
    })

