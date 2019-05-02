# Created by thanhpd on 3/13/2019
import logging
import unittest

import pytest

from wms import models as m
from wms.repositories import odoo_repo

_logger = logging.getLogger(__name__)


class OdooRepositoryTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OdooRepositoryTestCase, self).__init__(*args, **kwargs)
        self.odoo_1 = odoo_repo.OdooRepo()
        self.odoo_2 = odoo_repo.OdooRepo(target='cache', used_cache=True)

    @pytest.fixture
    def setup(self, mocker):
        mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)

    def test_connect_odoo_service_when_account_is_invalid_then_return_internal_error(
            self):
        pass

    def test_odoo_repo_function_name__parse_special_params(self):
        test_cases = [
            {
                'description': '',
                'input': {
                    'payload': {
                        'hello': 5,
                        'faker': 6
                    }
                },
                'expected': {
                    'payload': {
                        'hello': 5,
                        'faker': 6
                    }
                },

            },
            {
                'description': '',
                'input': {
                    'payload': {
                        'hello': 5,
                        'use_faker': True,
                        'no_cache': False,
                        'debug_mode': True
                    }
                },
                'expected': {
                    'payload': {
                        'hello': 5,
                    },

                },

            },
        ]

        # Test for the first case
        before_target = self.odoo_1._target
        before_used_cache = self.odoo_1._used_cache
        self.odoo_1._parse_special_params(test_cases[0]['input']['payload'])
        self.assertDictEqual(test_cases[0]['input']['payload'], test_cases[0]['expected']['payload'])
        self.assertEqual(self.odoo_1._target, before_target)
        self.assertEqual(self.odoo_1._used_cache, before_used_cache)

        # Test for the second case
        self.odoo_1._parse_special_params(test_cases[1]['input']['payload'])
        msg = "Payload should remove special value. Expect: (%s). Actual: (%s" % (
            test_cases[1]['expected']['payload'], test_cases[1]['input']['payload'])
        self.assertDictEqual(test_cases[1]['input']['payload'], test_cases[1]['expected']['payload'], msg=msg)
        self.assertTrue(self.odoo_2._special_params['use_faker'])
        self.assertTrue(self.odoo_2._special_params['debug_mode'])
        self.assertFalse(self.odoo_2._special_params['no_cache'])
