# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import services, models
from ..extensions import Namespace
from ..services import odoo_service

__author__ = 'MinhVlh'
_logger = logging.getLogger('api')

ns = Namespace('Teko Biz Type Location Detail', description='Teko Biz Type Location Detail')

# Define Schemas for Request and Response API decorator here
_teko_biz_type_location_detail_res = ns.model('teko_biz_type_location_detail_list_res', models.TekoBizTypeLocationDetailSchema.teko_biz_type_location_detail_res)



@ns.route('/', methods=['GET'])
class TekoBizTypeLocationDetail(_fr.Resource):
    @ns.marshal_with(_teko_biz_type_location_detail_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all warehouses
        :return: list[Warehouse]
        """
        print("Get Warehouse List")
        # print(json.dumps(request.args))
        data = request.args or request.json
        # warehouse_list = services.warehouse.get_warehouses(data)
        # return warehouse_list
        return odoo_service.call_odoo_repo('TekoBizTypeLocationDetail', 'list', data)


