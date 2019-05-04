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

_teko_biz_type_location_detail_req = ns.parser()
_teko_biz_type_location_detail_req.add_argument('warehouses', type=str, location='args', help='Warehouses code', action='split')
# _teko_biz_type_location_detail_req.add_argument('location_code', type=str, location='query', help='location code', action='split')


@ns.route('/', methods=['GET'])
class TekoBizTypeLocationDetail(_fr.Resource):
    @ns.expect(_teko_biz_type_location_detail_req, validate=True)
    @ns.marshal_with(_teko_biz_type_location_detail_res, as_list=True, skip_none=True, description="Successful Return")
    def get(self):
        """
        Get list teko biz type location detail
        :return: list[teko biz type location detail]
        """
        print("Get Warehouse List")
        warehouses = request.args.get("warehouses")
        if warehouses:
            warehouses.split(",")
        data={"warehouses":warehouses}

        return odoo_service.call_odoo_repo('TekoBizTypeLocationDetail', 'list', data)


