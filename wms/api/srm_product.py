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

ns = Namespace('srmProducts', description='SRM product operations')

# Define Schemas for Request and Response API decorator here
_srm_product_res = ns.model('srm_product_item_res', models.SrmProductSchema.srm_product_res)
_srm_product_req = ns.model('srm_product_item_req', models.SrmProductSchema.srm_product_req)

_error_res = ns.model('error_res', ErrorSchema.error_res)


@ns.route('/', methods=['GET', 'POST'])
class SrmProductLists(_fr.Resource):
    # @ns.marshal_with(_srm_product_res, as_list=True, description="Successful Return")
    # def get(self):
    #     """
    #     Get list all srm_products
    #     :return: list[SrmProduct]
    #     """
    #     print("Get SrmProduct List")
    #     # print(json.dumps(request.args))
    #     data = request.args or request.json
    #     srm_product_list = services.srm_product.get_srm_products(data)
    #     return srm_product_list

    @ns.expect(_srm_product_req, validate=True)
    @ns.marshal_with(_srm_product_res, as_list=False, description="Successful Creation")
    @ns.doc(
        responses={
            400: 'Nhóm sản phẩm không tồn tại',
            403: 'Insufficient permissions',
            500: 'Internal failure',
        }
    )
    def post(self):
        """
        Create a product
        :return: feId[SrmProduct]
        """
        data = request.args or request.json
        # rs = services.srm_product.create_srm_product(data)
        return odoo_service.call_odoo_repo('SrmProduct', 'create', data)


@ns.route('/<int:id>', methods=['PUT', 'DELETE'])
class SrmProductItem(_fr.Resource):
    @ns.expect(_srm_product_req, validate=True)
    @ns.marshal_with(_srm_product_res, as_list=False, description="Successful Update")
    def put(self, id):
        """
        Update a product
        :return: feId[SrmProduct]
        """
        data = request.args or request.json
        data['feId'] = id
        odoo_service.call_odoo_repo('SrmProduct', 'update', data)

    @ns.marshal_with(_srm_product_res, as_list=False, description="Successful Delete")
    def delete(self, id):
        """
        Delete a product
        :return: feId[SrmProduct]
        """
        return odoo_service.call_odoo_repo('SrmProduct', 'destroy', {'id': id})
