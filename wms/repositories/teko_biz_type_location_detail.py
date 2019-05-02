from .odoo_repo import OdooRepo


class TekoBizTypeLocationDetail(OdooRepo):
    _name = 'teko_biz_type_location_detail'
    _model = 'teko.biz.type.location.detail'

    _mapping = {
        'list': 'api_get_list_detail',
    }
