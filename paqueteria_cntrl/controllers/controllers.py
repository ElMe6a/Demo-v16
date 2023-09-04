# -*- coding: utf-8 -*-
# from odoo import http


# class PaqueteriaCntrl(http.Controller):
#     @http.route('/paqueteria_cntrl/paqueteria_cntrl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/paqueteria_cntrl/paqueteria_cntrl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('paqueteria_cntrl.listing', {
#             'root': '/paqueteria_cntrl/paqueteria_cntrl',
#             'objects': http.request.env['paqueteria_cntrl.paqueteria_cntrl'].search([]),
#         })

#     @http.route('/paqueteria_cntrl/paqueteria_cntrl/objects/<model("paqueteria_cntrl.paqueteria_cntrl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('paqueteria_cntrl.object', {
#             'object': obj
#         })
