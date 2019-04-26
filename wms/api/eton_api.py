# coding=utf-8
import logging
from ..extensions import Namespace
from flask_restplus import Resource
from ..models import EtonApiSchema
from ..services import odoo_service
from flask import request

__author__ = 'Huu'
_logger = logging.getLogger('api')

ns = Namespace('Eton', description='Eton APIs')

# Register Schemas for Request and Response API decorator here
ns.models[EtonApiSchema.eton_product.name] = EtonApiSchema.eton_product
ns.models[EtonApiSchema.eton_po_req.name] = EtonApiSchema.eton_po_req
ns.models[EtonApiSchema.eton_so_req.name] = EtonApiSchema.eton_so_req
ns.models[EtonApiSchema.eton_so_returned_req.name] = EtonApiSchema.eton_so_returned_req
ns.models[EtonApiSchema.eton_success_res.name] = EtonApiSchema.eton_success_res
ns.models[EtonApiSchema.eton_fail_res.name] = EtonApiSchema.eton_fail_res


@ns.route('/po/<int:id>', methods=['PUT'])
@ns.doc(params={'id': 'ID phiếu IN của stock.picking cần xử lý WMS'})
class ExternalPO(Resource):
    @ns.expect(EtonApiSchema.eton_po_req, validate=True)
    @ns.marshal_with(EtonApiSchema.eton_success_res, description='Operation succeed', code=200)
    @ns.marshal_with(EtonApiSchema.eton_fail_res, description='Operation failed', code=500)
    def put(self, id):
        data = request.get_json()
        data['_id'] = id
        repo_name = 'ExternalIncomingReceive'
        return odoo_service.call_odoo_repo(repo_name, 'create', data=data)


@ns.route('/so/<int:id>', methods=['PUT'])
@ns.doc(params={'id': 'ID phiếu Pick của stock.picking cần xử lý WMS'})
class ExternalSO(Resource):
    @ns.expect(EtonApiSchema.eton_so_req, validate=True)
    @ns.marshal_with(EtonApiSchema.eton_success_res, description='Successful updating', code=200)
    @ns.marshal_with(EtonApiSchema.eton_fail_res, description='Operation failed', code=500)
    def put(self, id):
        data = request.get_json()
        data['_id'] = id
        repo_name = None
        if data['eventType'] == 'picked':
            repo_name = 'ExternalOutgoingPicked'
        if data['eventType'] == 'packed':
            repo_name = 'ExternalOutgoingPacked'
        if data['eventType'] == 'delivered':
            repo_name = 'ExternalOutgoingDelivered'
        if data['eventType'] == 'returned':
            repo_name = 'ExternalOutgoingReturned'

        return odoo_service.call_odoo_repo(repo_name, 'create', data=data)


@ns.route('/so/<int:id>/returned', methods=['PUT'])
@ns.doc(params={'id': 'ID phiếu Pick của stock.picking cần xử lý WMS'})
class ExternalSOReturn(Resource):
    @ns.expect(EtonApiSchema.eton_so_returned_req, validate=True)
    @ns.marshal_with(EtonApiSchema.eton_success_res, description='Successful updating', code=200)
    @ns.marshal_with(EtonApiSchema.eton_fail_res, description='Operation failed', code=500)
    def put(self, id):
        data = request.get_json()
        data['_id'] = id
        repo_name = 'ExternalOutgoingReturned'
        return odoo_service.call_odoo_repo(repo_name, 'create', data=data)