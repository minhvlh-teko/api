# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import models
from ..services import odoo_service
from ..models.base import ErrorSchema
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Stock Out', description='StockOut operations')

# Define Schemas for Request and Response API decorator here
_stock_out_request_req = ns.model('stock_out_request_req', models.StockOutSchema.stock_out_request_req)
_stock_out_confirm_req = ns.model('stock_out_confirm_req', models.StockOutSchema.stock_out_confirm_req)

_error_res = ns.model('error_res', ErrorSchema.error_res)


@ns.route('/', methods=['POST', 'PUT'], )
class StockOut(_fr.Resource):
    @ns.expect(_stock_out_request_req, validate=True)
    @ns.marshal_with(_error_res, description='Confirm order request', code=200)
    @ns.marshal_with(_error_res, description='Order canceled', code=403)
    def post(self):
        """
        Request to pick up product
        """
        # print("Get StockOut List")

        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        return odoo_service.call_odoo_repo('StockOutRequest', 'create', data=data, module_name='stock_out')

    @ns.expect(_stock_out_confirm_req, validate=True)
    @ns.marshal_with(_error_res, description='Confirm order request', code=200)
    @ns.marshal_with(_error_res, description='Underselling', code=403)
    def put(self):
        """
        Confirm pick up product
        """
        # print("Get StockOut List")

        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        return odoo_service.call_odoo_repo('StockOutConfirm', 'create', data=data, module_name='stock_out')
