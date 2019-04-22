# coding=utf-8
import logging
from .odoo_repo import OdooRepo

__author__ = 'Son'
_logger = logging.getLogger('api')


class Location(OdooRepo):
    _name = 'locations'
    _model = 'stock.location'
    _mapping = {
        'list': 'api_get_list_detail',
    }
    _is_formalization = True

    def get_locations(self, data={}):
        """
        get list of location
        :return: list[Location]
        """
        return self.list(data)


class LocationMapping(OdooRepo):
    _name = 'location_mapping'
    _model = 'stock.location'
    _mapping = {
        'list': 'api_get_list_mapping',
    }

    def get_location_mapping(self, data={}):
        """
        get list of location
        :return: list[Location]
        """
        return self.list(data)

    def _formalize(self, response):
        """
        Override parent method
        :param response:
        :return:
        """
        response = super()._formalize(response)
        new_list = []
        for key in response:
            new_list.append({
                'code': key,
                'name': response[key]
            })
        return new_list
