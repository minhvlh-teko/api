from .odoo_repo import OdooRepo


class ExternalOutgoingPicked(OdooRepo):
    _name = 'ex_out_picked'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_external_outgoing_picked',
    }
