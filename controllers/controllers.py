# -*- coding: utf-8 -*-
from flectra import http

# class Epark(http.Controller):
#     @http.route('/epark/epark/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/epark/epark/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('epark.listing', {
#             'root': '/epark/epark',
#             'objects': http.request.env['epark.epark'].search([]),
#         })

#     @http.route('/epark/epark/objects/<model("epark.epark"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('epark.object', {
#             'object': obj
#         })