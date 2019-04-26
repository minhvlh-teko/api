# coding=utf-8
import logging

import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs

__author__ = 'Kien'
_logger = logging.getLogger('api')

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()


def init_app(app, **kwargs):
    """
    Extension initialization point
    :param flask.Flask app:
    :param kwargs:
    :return:
    """
    db.app = app
    db.init_app(app)
    migrate.init_app(app)
    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['ENV_MODE'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))


from .base import TimestampMixin

# Import all necesary models here
from .odoo_account import OdooAccount
from .wms_log import WmsLog
from .branch import BranchSchema, BranchMappingSchema
from .warehouse import WarehouseSchema, WarehouseMappingSchema
from .location import LocationSchema, LocationMappingSchema
from .srm_product import SrmProductSchema
from .stock_quant import StockQuantSchema
from .stock_out import StockOutSchema
from .eton_api import EtonApiSchema
