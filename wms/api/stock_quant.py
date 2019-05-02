# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import models
from ..services import odoo_service
from ..extensions import Namespace, exceptions

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Stock Quantities', description='StockQuant operations', validate=True)

# Define Schemas for Request and Response API decorator here
_stock_quant_item = ns.model('stock_quant_item', models.StockQuantSchema.stock_quant_item)
_stock_quant_item_min = ns.model('stock_quant_item_min', models.StockQuantSchema.stock_quant_item_min)


_stock_quant_res = ns.model('stock_quant_res', {
    'sku': _fr.fields.String(required=True, description='Product sku'),
    # 'items': _fr.fields.List(_fr.fields.Nested(_stock_quant_item, required=True))
    'items': _fr.fields.Nested(_stock_quant_item, allow_null=True, as_list=True, skip_none=True)
})

_stock_quant_min_res = ns.model('_stock_quant_item_min', {
    'sku': _fr.fields.String(required=True, description='Product sku'),
    # 'items': _fr.fields.List(_fr.fields.Nested(_stock_quant_item, required=True))
    'items': _fr.fields.Nested(_stock_quant_item_min, allow_null=True, as_list=True)
})

# add multi params
_stock_quant_req = ns.parser()
_stock_quant_req.add_argument('products', type=int, location='query', help='List sku', required=True, action='append')
_stock_quant_req.add_argument('regions', type=int, location='query', help='Regions', action='append')
_stock_quant_req.add_argument('branches', type=str, location='query', help='Branches', action='append')
_stock_quant_req.add_argument('warehouses', type=str, location='query', help='Warehouses code', action='append')
_stock_quant_req.add_argument('locations', type=str, location='query', help='Locations', action='append')


@ns.route('/', methods=['GET'], )
class StockQuants(_fr.Resource):
    @ns.expect(_stock_quant_req, validate=True)
    @ns.marshal_with(_stock_quant_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all stock quants
        :return: list[StockQuant]
        """
        # print("Get StockQuant List")

        data = request.args or request.json
        # validate products required
        if not data or not data['products']:
            raise exceptions.BadRequestException("Products is required")
        # print(json.dumps(data))
        # print(type(data))
        return odoo_service.call_odoo_repo('StockQuant', 'list', data)


@ns.route('/get_min', methods=['GET'], )
class StockQuantsOut(_fr.Resource):
    @ns.expect(_stock_quant_req, validate=True)
    @ns.marshal_with(_stock_quant_min_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all stock quants but for minimize properties
        :return: list[StockQuant]
        """
        # print("Get StockQuant List")

        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        return odoo_service.call_odoo_repo('StockQuant', 'list', data)
