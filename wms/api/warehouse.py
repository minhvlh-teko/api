# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import services, models
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Warehouses', description='Warehouse operations')

# Define Schemas for Request and Response API decorator here
_warehouse_res = ns.model('warehouse_list_res', models.WarehouseSchema.warehouse_res)
_warehouse_mapping_res = ns.model('warehouse_mapping_res', models.WarehouseMappingSchema.warehouse_mapping_res)


@ns.route('/', methods=['GET'])
class Warehouses(_fr.Resource):
    @ns.marshal_with(_warehouse_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all warehouses
        :return: list[Warehouse]
        """
        print("Get Warehouse List")
        # print(json.dumps(request.args))
        data = request.args or request.json
        warehouse_list = services.warehouse.get_warehouses(data)
        return warehouse_list


@ns.route('/mapping', methods=['GET'], doc=False)
class WarehouseMapping(_fr.Resource):
    @ns.marshal_with(_warehouse_mapping_res, as_list=True)
    def get(self):
        """
        Get list all warehouses mapping
        :return: list[Warehouse]
        """

        warehouse_mapping_list = services.warehouse.get_warehouse_mapping()
        return warehouse_mapping_list
