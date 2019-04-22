# coding=utf-8
import logging

import flask_restplus as _fr
from flask import request

from .. import models
from ..services import odoo_service
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')




class OdooCommon(_fr.Resource):
    _repo_name = ''
    _module_name = ''

    def post(self):
        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        if self._module_name:
            return odoo_service.call_odoo_repo(self._name, 'create', data=data, module_name=self._module_name)
        else:
            return odoo_service.call_odoo_repo(self._name, 'create', data=data)

    def put(self):
        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        if self._module_name:
            return odoo_service.call_odoo_repo(self._name, 'update', data=data, module_name=self._module_name)
        else:
            return odoo_service.call_odoo_repo(self._name, 'update', data=data)

    def get(self):
        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        if self._module_name:
            return odoo_service.call_odoo_repo(self._name, 'list', data=data, module_name=self._module_name)
        else:
            return odoo_service.call_odoo_repo(self._name, 'retrieve', data=data)

    def delete(self):
        data = request.args or request.json
        # print(json.dumps(data))
        # print(type(data))
        if self._module_name:
            return odoo_service.call_odoo_repo(self._name, 'delete', data=data, module_name=self._module_name)
        else:
            return odoo_service.call_odoo_repo(self._name, 'delete', data=data)
