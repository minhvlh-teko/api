# coding=utf-8
import logging

from flask import request
from .odoo_common import OdooCommon

from .. import services, models
from ..extensions import Namespace

__author__ = 'SonLp'
_logger = logging.getLogger('api')

ns = Namespace('Internal', description='Internal API operations')


@ns.route('/accountTag', methods=['POST', 'PUT', 'DELETE'], doc=False)
@ns.hide
class AccountAccountTag(OdooCommon):
    _repo_name = 'AccountAccountTag'


@ns.route('/accountTemplate', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountTemplate(OdooCommon):
    _repo_name = 'AccountAccountTemplate'


@ns.route('/accountType', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountAccountType(OdooCommon):
    _repo_name = 'AccountAccountType'


@ns.route('/account', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountAccount(OdooCommon):
    _repo_name = 'AccountAccount'


@ns.route('/accountGroup', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountGroup(OdooCommon):
    _repo_name = 'AccountGroup'


@ns.route('/accountInvoice', methods=['PUT'], doc=False)
class AccountInvoice(OdooCommon):
    _repo_name = 'AccountInvoice'


@ns.route('/accountJournal', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountJournal(OdooCommon):
    _repo_name = 'AccountJournal'


@ns.route('/accountPaymentTerm', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountPaymentTerm(OdooCommon):
    _repo_name = 'AccountPaymentTerm'


@ns.route('/accountPaymentTermLine', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountPaymentTermLine(OdooCommon):
    _repo_name = 'AccountPaymentTermLine'


@ns.route('/accountTax', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountTax(OdooCommon):
    _repo_name = 'AccountTax'


@ns.route('/accountTaxGroup', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountTaxGroup(OdooCommon):
    _repo_name = 'AccountTaxGroup'


@ns.route('/accountTaxTemplate', methods=['POST', 'PUT', 'DELETE'], doc=False)
class AccountTaxTemplate(OdooCommon):
    _repo_name = 'AccountTaxTemplate'


# External route !
# @ns.route('/externalIncomingReceived', methods=['POST'], doc=False)
# class ExternalIncomingReceived(OdooCommon):
#     _repo_name = 'ExternalIncomingReceived'
#
#
# @ns.route('/externalOutgoingDelivered', methods=['POST'], doc=False)
# class ExternalOutgoingDelivered(OdooCommon):
#     _repo_name = 'ExternalOutgoingDelivered'
#
#
# @ns.route('/externalOutgoingPacked', methods=['POST'], doc=False)
# class ExternalOutgoingPacked(OdooCommon):
#     _repo_name = 'ExternalOutgoingPacked'
#
#
# @ns.route('/externalOutgoingPicked', methods=['POST'], doc=False)
# class ExternalOutgoingPicked(OdooCommon):
#     _repo_name = 'ExternalOutgoingPicked'
#
#
# @ns.route('/externalOutgoingReturned', methods=['POST'], doc=False)
# class ExternalOutgoingReturned(OdooCommon):
#     _repo_name = 'ExternalOutgoingReturned'


@ns.route('/loBlDelivered', methods=['POST'], doc=False)
class LoBlDelivered(OdooCommon):
    _repo_name = 'LoBlDelivered'


@ns.route('/loBlReturning', methods=['POST'], doc=False)
class LoBlReturning(OdooCommon):
    _repo_name = 'LoBlReturning'


@ns.route('/mrpBom', methods=['POST', 'PUT', 'DELETE'], doc=False)
class MrpBom(OdooCommon):
    _repo_name = 'MrpBom'


@ns.route('/poLine', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PoLine(OdooCommon):
    _repo_name = 'PoLine'


@ns.route('/poReceipt', methods=['POST'], doc=False)
class PoReceipt(OdooCommon):
    _repo_name = 'PoReceipt'


@ns.route('/poType', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PoType(OdooCommon):
    _repo_name = 'PoType'


@ns.route('/poTypeDetail', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PoTypeDetail(OdooCommon):
    _repo_name = 'PoTypeDetail'


@ns.route('/porPrices', methods=['GET', 'POST'], doc=False)
class PorPrices(OdooCommon):
    _repo_name = 'PorPrices'


@ns.route('/porReceipt', methods=['POST'], doc=False)
class PorReceipt(OdooCommon):
    _repo_name = 'PorReceipt'


@ns.route('/porType', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PorType(OdooCommon):
    _repo_name = 'PorType'


@ns.route('/porTypeDetail', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PorTypeDetail(OdooCommon):
    _repo_name = 'PorTypeDetail'


@ns.route('/productAttribute', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductAttribute(OdooCommon):
    _repo_name = 'ProductAttribute'


@ns.route('/productAttributeValue', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductAttributeValue(OdooCommon):
    _repo_name = 'ProductAttributeValue'


@ns.route('/productBrand', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductBrand(OdooCommon):
    _repo_name = 'ProductBrand'


@ns.route('/productCategory', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductCategory(OdooCommon):
    _repo_name = 'ProductCategory'


@ns.route('/productPricelist', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductPricelist(OdooCommon):
    _repo_name = 'ProductPricelist'


@ns.route('/productPricelistItem', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductPriceListItem(OdooCommon):
    _repo_name = 'ProductPricelistItem'


@ns.route('/product', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductProduct(OdooCommon):
    _repo_name = 'ProductProduct'


@ns.route('/productSaleBranch', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductSaleBranch(OdooCommon):
    _repo_name = 'ProductSaleBranch'


@ns.route('/productSupplierInfo', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductSupplierInfo(OdooCommon):
    _repo_name = 'ProductSupplierInfo'


@ns.route('/productTemplate', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductTemplate(OdooCommon):
    _repo_name = 'ProductTemplate'


@ns.route('/productUom', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductUom(OdooCommon):
    _repo_name = 'ProductUom'


@ns.route('/productUomCateg', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ProductUomCateg(OdooCommon):
    _repo_name = 'ProductUomCateg'


@ns.route('/purchaseOrder', methods=['POST', 'PUT', 'DELETE'], doc=False)
class PurchaseOrder(OdooCommon):
    _repo_name = 'PurchaseOrder'


@ns.route('/resPartnerBank', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ResPartnerBank(OdooCommon):
    _repo_name = 'ResPartnerBank'


@ns.route('/resPartnerCategory', methods=['POST', 'PUT', 'DELETE'], doc=False)
class ResPartnerCategory(OdooCommon):
    _repo_name = 'ResPartnerCategory'


@ns.route('/saleOrder', methods=['POST', 'PUT'], doc=False)
class SaleOrder(OdooCommon):
    _repo_name = 'SaleOrder'


@ns.route('/stockInventoryThreshold', methods=['POST', 'PUT', 'DELETE'], doc=False)
class StockInventoryThreshold(OdooCommon):
    _repo_name = 'StockInventoryThreshold'


# Connect direct to Odoo dbs !!
# @ns.route('/stockQuantWms', methods=['GET'], doc=False)
# class StockQuantWms(OdooCommon):
#     _repo_name = 'StockQuantWms'


@ns.route('/stockTransfer', methods=['POST'], doc=False)
class StockTransfer(OdooCommon):
    _repo_name = 'StockTransfer'


# Connect direct to Odoo dbs !!
# @ns.route('/stockTransferStatus', methods=['POST', 'PUT', 'DELETE'], doc=False)
# class StockTransferStatus(OdooCommon):
#     _repo_name = 'StockTransferStatus'


@ns.route('/supplier', methods=['POST', 'PUT', 'DELETE'], doc=False)
class Supplier(OdooCommon):
    _repo_name = 'Supplier'


@ns.route('/tekoProductBizType', methods=['POST', 'PUT', 'DELETE'], doc=False)
class TekoProductBizType(OdooCommon):
    _repo_name = 'TekoProductBizType'


@ns.route('/tekoProductStatus', methods=['POST', 'PUT', 'DELETE'], doc=False)
class TekoProductStatus(OdooCommon):
    _repo_name = 'TekoProductStatus'


# Connect direct to Odoo dbs !!
# @ns.route('/verifyReceipt', methods=['POST', 'PUT', 'DELETE'], doc=False)
# class VerifyReceipt(OdooCommon):
#     _repo_name = 'VerifyReceipt'


# Connect direct to Odoo dbs !!
# @ns.route('/wmsSaleOrderStatus', methods=['POST', 'PUT', 'DELETE'], doc=False)
# class WmsSaleOrderStatus(OdooCommon):
#     _repo_name = 'WmsSaleOrderStatus'
