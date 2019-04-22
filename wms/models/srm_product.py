# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class SrmProductSchema:
    srm_product = {
        # 'fe_id': fields.Integer(required=True, description='Mã sản phẩm tạo tại seller_center'),
        'defaultCode': fields.String(required=True, description='Mã'),
        'name': fields.String(required=True, description='Tên'),
        'shortName': fields.String(required=False, description='Tên tính năng'),
        'partNumber': fields.String(required=False, description='Part Number'),
        'attributeValueCode': fields.String(required=False, description='Thuộc tính (màu sắc)'),
        'type': fields.String(required=True, description='Loại sản phẩm:\
- consu: Sản phẩm không quản lý tồn kho (Cho phép bán âm)\
- product: Sản phẩm có quản lý tồn & lưu kho', enum=['consu','product']),

        'barcode': fields.String(required=True, description='Mã vạch'),
        'productBrandCode': fields.String(required=True, description='Thương hiệu'),
        'categCode': fields.String(required=True, description='Nhóm sản phẩm'),
        'uomName': fields.String(required=True, description='Đơn vị tính'),
        'uomPoName': fields.String(required=True, description='Đơn vị đo lường mua hàng'),
        'salePoint': fields.Float(required=False, description='Điểm sản phẩm'),
        'warrantyPeriod': fields.Float(required=False, description='Thời gian bảo hành'),
        'warrantyNote': fields.String(required=False, description='Ghi chú bảo hành'),
        'exchangePeriod': fields.Integer(required=False, description='Một đổi 1 trong (ngày)'),
        'warrantyStamp_qty': fields.Integer(required=False, description='Số lượng tem bảo hành'),
        'saleOnlineOnly': fields.Boolean(required=True, description='Chỉ bán online', default=False),
        'supportDelivery': fields.Boolean(required=True, description='Hỗ trợ giao hàng', default=False),
        'productStatus': fields.Integer(required=False, description='Trạng thái'),
        'costPriceCalc': fields.Boolean(required=True, description='Tính giá thành', default=False),
        'tracking': fields.String(required=True, description='tracking', default=None),
        'note': fields.String(required=False, description='Ghi chú'),
        'isUncounted': fields.Boolean(required=True, description='Không kiểm đếm', default=False),
        'isService': fields.Boolean(required=True, description='Sản phẩm dịch vụ', default=False),
    }

    srm_product_req = srm_product.copy()
    srm_product_res = {
        'feId': fields.Integer(required=True, description='Mã sản phẩm tạo tại seller_center'),
    }

