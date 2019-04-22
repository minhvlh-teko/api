# coding=utf-8
import logging
from .odoo_repo import OdooRepo

__author__ = 'Son'
_logger = logging.getLogger('api')


class StockOutRequest(OdooRepo):
    _name = 'stock_out_request'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_stock_out_request',
    }
    _is_formalization = True

    def _formalize(self, response):
        """
        Override parent method
        :param dict response:
        :return: dict
        """
        return super()._formalize(response)


class StockOutConfirm(OdooRepo):
    _name = 'stock_out_confirm'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_stock_out_confirm',
    }
    _is_formalization = True

    def _formalize(self, response):
        """
        Override parent method
        :param dict response:
        :return: dict
        """
        print(response)
        return super()._formalize(response)
