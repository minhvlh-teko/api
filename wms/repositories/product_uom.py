import logging

from .odoo_repo import OdooRepo


_logger = logging.getLogger('api')


class ProductUom(OdooRepo):
    _name = 'product_uom'
    _model = 'product.uom'
