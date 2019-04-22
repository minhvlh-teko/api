import logging

import coreapi
import coreschema
from rest_framework.exceptions import ValidationError
from rest_framework.schemas import ManualSchema

from .odoo_repo import OdooRepo


_logger = logging.getLogger('api')

manual_schema = ManualSchema(fields=[
    coreapi.Field(
        "products", required=True, location="path",
        schema=coreschema.String(description='Products Codes, separated by comma')
    ),
    coreapi.Field(
        "partner", required=True, location="path",
        schema=coreschema.String(description="Partner Id, separated by comma")
    )
])


class PorPrice(OdooRepo):
    _name = 'por_prices'
    _model = 'product.product'
    _mapping = {
        'list': 'api_get_por_price',
        'create': 'api_get_por_price',  # support POST method for long list of products
    }
    schema = manual_schema

    def _parse_payload(self, request):

        super()._parse_payload(request)

        if self._api_method not in ('list', 'create'):
            return

        params = request.data if self._api_method == 'create' else request.query_params

        product_codes = params.get('products')
        partner_id = params.get('partner')

        if not product_codes:
            raise ValidationError('Param `products` is required')
        if not partner_id:
            raise ValidationError('Param `partner` is required')

        product_codes = product_codes.split(',')

        self._payload = {
            'products': product_codes,
            'partner': partner_id
        }
