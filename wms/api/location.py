# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import services, models
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Locations', description='Location operations')

# Define Schemas for Request and Response API decorator here
_location_res = ns.model('location_list_res', models.LocationSchema.location_res)
_location_mapping_res = ns.model('location_mapping_res', models.LocationMappingSchema.location_mapping_res)


@ns.route('/', methods=['GET'])
class Locations(_fr.Resource):
    @ns.marshal_with(_location_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all locations
        :return: list[Location]
        """
        print("Get Location List")
        # print(json.dumps(request.args))
        data = request.args or request.json
        location_list = services.location.get_locations(data)
        return location_list


@ns.route('/mapping', methods=['GET'], doc=False)
class LocationMapping(_fr.Resource):
    @ns.marshal_with(_location_mapping_res, as_list=True)
    def get(self):
        """
        Get list all locations mapping
        :return: list[Location]
        """

        location_mapping_list = services.location.get_location_mapping()
        return location_mapping_list
