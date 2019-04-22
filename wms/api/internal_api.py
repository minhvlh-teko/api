# coding=utf-8
import logging

from flask import request
from .odoo_common import OdooCommon

from .. import services, models
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('internal', description='Internal API operations')


@ns.route('/accountTag', methods=['POST', 'PUT', 'DELETE'], doc=False)
@ns.hide
class AccountAccountTag(OdooCommon):
    _repo_name = 'AccountAccountTag'


@ns.route('/accountTemplate', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountTemplate(OdooCommon):
    _repo_name = 'AccountAccountTag'


@ns.route('/accountType', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountAccountType(OdooCommon):
    _repo_name = 'AccountAccountType'


@ns.route('/account', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountAccount(OdooCommon):
    _repo_name = 'AccountAccount'


@ns.route('/accountGroup', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountGroup(OdooCommon):
    _repo_name = 'AccountGroup'
