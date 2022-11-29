# -*- coding: utf-8 -*-
# from odoo import http


# class CttDomicilio(http.Controller):
#     @http.route('/ctt_domicilio/ctt_domicilio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ctt_domicilio/ctt_domicilio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ctt_domicilio.listing', {
#             'root': '/ctt_domicilio/ctt_domicilio',
#             'objects': http.request.env['ctt_domicilio.ctt_domicilio'].search([]),
#         })

#     @http.route('/ctt_domicilio/ctt_domicilio/objects/<model("ctt_domicilio.ctt_domicilio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ctt_domicilio.object', {
#             'object': obj
#         })
