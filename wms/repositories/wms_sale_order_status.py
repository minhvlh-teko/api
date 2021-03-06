import logging

# from django.db import connections
# from rest_framework.exceptions import ValidationError
# from rest_framework.response import Response

from .odoo_repo import OdooRepo

_logger = logging.getLogger('api')


class WmsSaleOrderStatus(OdooRepo):
    _name = 'wms_sale_order_status'
"""
    def _parse_payload(self, request):
        super()._parse_payload(request)

        if self._api_method == 'list':
            request_codes = request.query_params.get('requestCodes')
            if not request_codes:
                raise ValidationError('Param `requestCodes` is required')

            self._payload['request_codes'] = request_codes.split(',')

    def _call_api(self):
        request_codes = self._payload['request_codes']

        cursor = connections['wms'].cursor()

        cursor.execute("SELECT id, code FROM sale_order_service_status;")

        service_status = {record[0]: record[1] for record in cursor}

        cursor.execute(
            "SELECT client_order_ref, tk_service_status, write_date, id FROM sale_order WHERE client_order_ref IN %s;",
            [tuple(request_codes)])

        data = {record[0]: {
            'id': record[3],
            'status': service_status[record[1]],
            'last_update_date': record[2].__str__(),
        } for record in cursor}

        return {
            'code': 0,
            'message': 'OK',
            'data': data,
        }

    def _handle(self, request, *args, **kwargs):
        try:
            self._parse_payload(request)

            response = self._call_api()

            return Response(response)

        except Exception as e:
            _logger.exception('[%s@%s] FAILED' % (self._name, self._api_method))
            return Response(repr(e), status=500)
"""