from .odoo_repo import OdooRepo


class ExternalOutgoingDelivered(OdooRepo):
    _name = 'ex_out_delivered'
    _model = 'stock.picking'
    _mapping = {
        'create': 'api_external_outgoing_delivered',
    }
