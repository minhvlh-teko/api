from .odoo_repo import OdooRepo


class ExternalOutgoingReturned(OdooRepo):
    _name = 'ex_out_returned'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_external_outgoing_returned',
    }
