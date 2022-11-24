# -*- coding: utf-8 -*-
# from odoo import http


# class TortiConfig(http.Controller):
#     @http.route('/torti_config/torti_config', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/torti_config/torti_config/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('torti_config.listing', {
#             'root': '/torti_config/torti_config',
#             'objects': http.request.env['torti_config.torti_config'].search([]),
#         })

#     @http.route('/torti_config/torti_config/objects/<model("torti_config.torti_config"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('torti_config.object', {
#             'object': obj
#         })
