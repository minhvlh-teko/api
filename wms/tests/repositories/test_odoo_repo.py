# Created by thanhpd on 3/13/2019
import logging
import unittest

import pytest

from wms import models as m, repositories

_logger = logging.getLogger(__name__)



class OdooRepositoryTestCase(unittest.TestCase):
    @pytest.fixture
    def setup(self, mocker):
        mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)

    def test_connect_odoo_service_when_account_is_invalid_then_return_internal_error(
            self):
        pass

