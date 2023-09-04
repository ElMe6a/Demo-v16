# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class paqueteria_cntrl(models.Model):
#     _name = 'paqueteria_cntrl.paqueteria_cntrl'
#     _description = 'paqueteria_cntrl.paqueteria_cntrl'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
