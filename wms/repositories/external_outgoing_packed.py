from .odoo_repo import OdooRepo


class ExternalOutgoingPacked(OdooRepo):
    _name = 'ex_out_packed'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_external_outgoing_packed',
    }
