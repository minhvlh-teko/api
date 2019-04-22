# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class WarehouseSchema:
    warehouse = {
        'code': fields.String(required=True, description='warehouse code'),
        'name': fields.String(required=False, description='warehouse name'),
        'branchCode': fields.String(required=False, description='warehouse branch code'),
    }

    warehouse_res = warehouse.copy()
    warehouse_req = {}


class WarehouseMappingSchema:
    warehouse_mapping_res = {
        'code': fields.String(required=True, description='warehouse code'),
        'name': fields.String(required=False, description='warehouse name'),
    }
