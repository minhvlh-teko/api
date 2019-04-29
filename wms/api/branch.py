# coding=utf-8
import logging
import json

import flask_restplus as _fr
from flask import request

from .. import services, models
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Branches', description='Branch operations')

# Define Schemas for Request and Response API decorator here
_branch_res = ns.model('branch_list_res', models.BranchSchema.branch_res)
_branch_mapping_res = ns.model('branch_mapping_res', models.BranchMappingSchema.branch_mapping_res)


@ns.route('/', methods=['GET'])
class Branches(_fr.Resource):
    @ns.marshal_with(_branch_res, as_list=True, description="Successful Return")
    def get(self):
        """
        Get list all branches
        :return: list[Branch]
        """
        print("Get Branch List")
        # print(json.dumps(request.args))
        data = request.args or request.json
        branch_list = services.branch.get_branches(data)
        return branch_list


@ns.route('/mapping', methods=['GET'], doc=False)
class BranchMapping(_fr.Resource):
    @ns.marshal_with(_branch_res, as_list=True)
    def get(self):
        """
        Get list all branches mapping
        :return: list[Branch]
        """

        branch_mapping_list = services.branch.get_branch_mapping()
        return branch_mapping_list
