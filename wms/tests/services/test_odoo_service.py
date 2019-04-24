# Created by thanhpd on 3/11/2019
import logging
import unittest
from unittest.mock import patch

import pytest

from wms.extensions.exceptions import BadRequestException
from wms.services import odoo_service

_logger = logging.getLogger(__name__)


class OdooServiceTest(unittest.TestCase):
    def test_odoo_service_when_send_wrong_method_then_raise_exception(self):
        pass
