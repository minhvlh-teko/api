# coding=utf-8
import logging
# import json

import flask_restplus as _fr
from flask import request

from .. import models
from ..services import odoo_service
from ..extensions import Namespace
from ..models.base import ErrorSchema

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('SRM Products', description='SRM product operations')

# Define Schemas for Request and Response API decorator here
_srm_product_res = ns.model('srm_product_item_res', models.SrmProductSchema.srm_product_res)
_srm_product_req = ns.model('srm_product_item_req', models.SrmProductSchema.srm_product_req)

_error_res = ns.model('error_res', ErrorSchema.error_res)


@ns.route('/', methods=['GET', 'POST'])
class SrmProductLists(_fr.Resource):
    @ns.expect(_srm_product_req, validate=True)
    @ns.marshal_with(_error_res, as_list=False, description="Successful Creation", code=200)
    @ns.marshal_with(_error_res, description='Category does not exist', code=400)
    @ns.marshal_with(_error_res, description='Insufficient permissions', code=403)
    @ns.marshal_with(_error_res, description='Internal failure', code=500)
    def post(self):
        """
        Create a product
        """
        data = request.args or request.json
        # rs = services.srm_product.create_srm_product(data)
        return odoo_service.call_odoo_repo('SrmProduct', 'create', data)


@ns.route('/<int:id>', methods=['PUT', 'DELETE'])
class SrmProductItem(_fr.Resource):
    @ns.expect(_srm_product_req, validate=True)
    @ns.marshal_with(_error_res, as_list=False, description="Successful Update")
    def put(self, id):
        """
        Update a product
        """
        data = request.args or request.json
        data['feId'] = id
        odoo_service.call_odoo_repo('SrmProduct', 'update', data)

    @ns.marshal_with(_error_res, as_list=False, description="Successful Delete")
    def delete(self, id):
        """
        Delete a product
        """
        return odoo_service.call_odoo_repo('SrmProduct', 'destroy', {'id': id})
