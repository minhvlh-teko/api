from .odoo_repo import OdooRepo


class ExternalIncomingReceived(OdooRepo):
    _name = 'ex_in_received'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_external_incoming_received',
    }
