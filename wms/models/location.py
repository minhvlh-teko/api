# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class LocationSchema:
    location = {
        'code': fields.String(required=True, description='location code'),
        'name': fields.String(required=False, description='location name'),
        'parentCode': fields.String(required=True, description='location parent code'),
    }

    location_res = location.copy()
    location_req = {}


class LocationMappingSchema:
    location_mapping_res = {
        'code': fields.String(required=True, description='location code'),
        'name': fields.String(required=False, description='location name'),
    }
