# coding=utf-8
import logging
import re

import odoorpc
import xmlrpc.client as xc
from ..models import OdooAccount
from ..extensions import exceptions
from werkzeug.datastructures import ImmutableMultiDict

from flask import request

__author__ = 'Son'
_logger = logging.getLogger('api')


class OdooRepo:
    """
    This Repo is the port to connect and get api from Odoo
    """
    _api_method = None
    _client_ip = None
    _cors_allow = ''
    _name = 'odoo_repo'
    _odoo = None
    _model = None
    _mapping = {
        'create': 'api_create_from_msg',
        'update': 'api_update_from_msg',
        'delete': 'api_delete_from_msg',
    }
    '''if this param is set to true, all requests and responses param will be standardlized'''
    _is_formalization = False

    def __init__(self):
        pass

    def _get_account(self, client_ip):
        """
        GEt odoo account to loggin and get data from api
        :param client_ip: string ip
        :return: [OdooAccount] account info
        """
        account = OdooAccount.query.filter(
            OdooAccount.client_ip.ilike('%{0}%'.format(client_ip))
        ).first()
        if account:
            return account
        raise exceptions.UnAuthorizedException('Client IP not authenticate!')

    def _get_account_by_secret(self):
        """
        Use for public API to access if secret key is exist and not null
        :param secret_key:
        :return: account info
        """

        if not self._is_using_secret_key():
            raise exceptions.ForbiddenException('Cannot access function _get_account_by_secret when secret key is null')

        account = OdooAccount.objects.filter(secret_key=self._secret_key).filter(api_list__contains=self._name)

        if account:
            return account[0]
        raise exceptions.UnAuthorizedException('Secret Key is invalid!')

    def _is_using_secret_key(self):
        """
        Check if this API using Secret Key for Public API or not
        :return: True if this API use secret key
        """
        if self._secret_key is not None and self._secret_key:
            return True
        else:
            return False

    def _update_secret_key_info(self):
        """
        If params of request have secret_key value then update to the system
        :return: None
        """
        params = self._payload
        secret_key = params.get('secret_key')
        if secret_key is None or not secret_key:
            self._secret_key = None
        else:
            self._secret_key = secret_key

    def _get_client_ip(self):
        if self._client_ip is None:
            x_forwarded_for = request.headers.getlist('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                self._client_ip = x_forwarded_for.split(',')[0]
            else:
                self._client_ip = request.remote_addr

        return self._client_ip

    def _get_odoo_client(self):
        if self._odoo is None:
            self._odoo = self._connect()
        return self._odoo

    def _handle(self, rq_data, *args, **kwargs):
        """
        Manage all all request handle here
        :param rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        _logger.info('[%s@%s] Called by <%s>...' % (self._name, self._api_method, self._get_client_ip()))
        # get data params
        self._parse_payload(rq_data)
        # make all data to underscope style
        if self._is_formalization:
            self._apply_underscore_to_dict(self._payload)

        _logger.debug('[%s@%s] Payload:\n%s' % (self._name, self._api_method, self._payload))

        try:

            if not (self._model and self._mapping and self._mapping.get(self._api_method)):
                return exceptions.NotFoundException("Endpoint is not defined.")

            _logger.info('Payload %s', self._payload)

            response = self._call_api()

            _logger.info('[%s@%s] Completed.' % (self._name, self._api_method))
            rs_data = self._formalize(response)

            return rs_data

            # Set response header CORS for public API
            # if self._cors_allow:
            #     header = {
            #         "Access-Control-Allow-Origin": self._cors_allow
            #     }
            #     return Response(response, None, None, header)
            # else:
            #     return Response(response)

        except Exception as e:
            _logger.exception('[%s@%s] FAILED' % (self._name, self._api_method))
            # raise exceptions.global_error_handler(e)
            raise e

    def _validate(self, response):
        """
        Validate data response and formalization
        :param response: dict data return from Odoo
        :return: Dict, necessary data to return
        """

        if isinstance(response, dict) and response.get("message") and response.get("message") == 'OK':
            if response.get("data"):
                return self._apply_camelcase_to_dict(response.get("data")) if self._is_formalization else response.get(
                    "data")
            else:
                return {}
        else:

            msg = "There is a problem with response format"
            _logger.debug(msg)
            if response.get("message"):
                msg = response.get("message")
            raise exceptions.HTTPException(message=msg)

    def _call_api(self):
        """
        Call API to Odoo
        :return: dict[Response data]
        """

        try:
            # Update secret key if available, should add to init functions
            self._update_secret_key_info()
            # Check whether using Secret Key  or Using IP to get API account
            if self._is_using_secret_key():
                account = self._get_account_by_secret()
                # Only set response header when using Public API
                self._cors_allow = account.cors_allow
            else:
                client_ip = self._get_client_ip()
                account = self._get_account(client_ip)

            if account.port != 443:
                url = 'http://{0}:{1}'.format(account.url, account.port)
            else:
                url = 'https://{0}'.format(account.url)
            if not account.uid:
                common = xc.ServerProxy('{}/xmlrpc/2/common'.format(url))
                account.uid = common.authenticate(account.dbs, account.user, account.password, {})
                account.save()
            _logger.info("Prepare to send to odoo")
            models = xc.ServerProxy('{}/xmlrpc/2/object'.format(url), allow_none=True)
            return models.execute_kw(account.dbs, account.uid, account.password,
                                     self._model, self._mapping.get(self._api_method),
                                     [self._payload])
        except Exception as e:
            _logger.info('Failed to authenticate error= %s', repr(e))
            raise ValueError('Exception: %s' % repr(e))

    def _connect(self):
        try:
            client_ip = self._get_client_ip()
            account = self._get_account(client_ip)
            odoo = odoorpc.ODOO(account.url, port=account.port)
            odoo.login(account.dbs, account.user, account.password)
            _logger.info('Success authentication user %s', odoo.env.user.name)
            return odoo
        except Exception as e:
            _logger.info('Failed to authenticate error= %s', repr(e))
            raise exceptions.UnAuthorizedException('Can not authentication! Client IP: %s' % client_ip)

    def create(self, rq_data, *args, **kwargs):
        """
        Apply for Post method
        :param dict|list rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        self._api_method = 'create'
        return self._handle(rq_data, *args, **kwargs)

    def retrieve(self, rq_data, *args, **kwargs):
        """
        Apply for GET one item method
        :param dict|list rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        self._api_method = 'retrieve'
        return self._handle(rq_data, *args, **kwargs)

    def list(self, rq_data, *args, **kwargs):
        """
        Apply for GET a list of item Method
        :param dict|list rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        self._api_method = 'list'
        return self._handle(rq_data, *args, **kwargs)

    def update(self, rq_data, *args, **kwargs):
        """
        Apply for PUT method
        :param dict|list rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        self._api_method = 'update'
        return self._handle(rq_data, *args, **kwargs)

    def destroy(self, rq_data, *args, **kwargs):
        """
        Apply DELETE method
        :param dict|list rq_data:
        :param args:
        :param kwargs:
        :return:
        """
        self._api_method = 'delete'
        return self._handle(rq_data, *args, **kwargs)

    def _parse_payload(self, rq_data):
        """
        Parse payload from data input
        :param rq_data:
        :return:
        """
        payload = rq_data
        if isinstance(payload, ImmutableMultiDict):
            payload = payload.to_dict(flat=False)

        if payload:
            self._payload = payload
        else:
            self._payload = {}

    def _to_underscore(self, name):
        """
        Convert ( Lower) Camelcase to underscore
        :param  str name: string to be converted
        :return:
        """
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _to_camel_case(self, snake_str):
        """
        Convert unserscore to camel case
        :param str snake_str: string to be converted
        :return:
        """
        components = snake_str.split('_')
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + ''.join(x.title() for x in components[1:])

    def _apply_underscore_to_dict(self, dict_item):
        """
        under score for all key of a dict (using reference variable)
        :param dict|list dict_item: dictionary or list object to be converted
        :return: dict
        """
        if isinstance(dict_item, dict):
            for key in dict_item:
                item = dict_item.pop(key)
                dict_item[self._to_camel_case(key)] = item
                if isinstance(item, dict) or isinstance(item, list):
                    self._apply_underscore_to_dict(item)

        if isinstance(dict_item, list):
            for item in dict_item:
                if isinstance(item, dict) or isinstance(item, list):
                    self._apply_underscore_to_dict(item)

    def _apply_camelcase_to_dict(self, dict_item):
        """
        under score for all key of a dict (using reference variable)
        :param dict|list dict_item: dictionary or list object to be converted
        :return: dict|list
        """
        if isinstance(dict_item, dict):
            for key in dict_item:
                item = dict_item.pop(key)
                dict_item[self._to_camel_case(key)] = item
                if isinstance(item, dict) or isinstance(item, list):
                    self._apply_camelcase_to_dict(item)

        if isinstance(dict_item, list):
            for item in dict_item:
                if isinstance(item, dict) or isinstance(item, list):
                    self._apply_camelcase_to_dict(item)
        return dict_item

    def _formalize(self, response):
        """
        Abstract method to reformat response following good rule
        :param dict response: odoo response data
        :return: dict
        """
        return self._validate(response)

    def _parse_by_template(self, content, mapping):
        """
        Define emplate and add content to payload
        :param content:
        :param mapping:
        :return:
        """
        response = {}

        for key, val in mapping.items():
            response[key] = iterate_dictionary(content, val)
            # Because all return list as value so we must get real value
            if response[key] is not None and len(response[key]) == 1 and not isinstance(response[key][0], dict):
                response[key] = response[key][0]

        return response
