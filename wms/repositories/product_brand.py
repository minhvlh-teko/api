import logging

from .odoo_repo import OdooRepo


_logger = logging.getLogger('api')


class ProductBrand(OdooRepo):
    _name = 'brands'
    _model = 'product.brand'
