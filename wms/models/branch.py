# coding=utf-8

import logging

from flask_restplus import fields

__author__ = 'SonLp'
_logger = logging.getLogger('api')


class BranchSchema:
    branch = {
        'code': fields.String(required=True, description='branch code'),
        'name': fields.String(required=False, description='branch name'),
    }

    branch_res = branch.copy()
    branch_req = {}


class BranchMappingSchema:
    branch_mapping_res = {
        'code_1': fields.String(required=False, description='branch name'),
        'code_2': fields.String(required=False, description='branch name'),
        'code_n': fields.String(required=False, description='branch name')
    }
