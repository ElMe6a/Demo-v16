from odoo import models, fields, api, _
import logging
import json
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
import datetime

class recoleccion(models.Model):
    _name = 'torti_config.recolecciones'
    _description = 'Recoleccion de Efectivo'
    _order = 'id desc'
     
    fecha_retiro = fields.Datetime(
        string="Fecha de Retiro"
    )
    sucursal = fields.Char(
        string="Sucursal"
    )
    monto = fields.Float(
        string="Monto de Retiro"
    )
    motivo = fields.Char(
        string="Motivo de Retiro"
    )
#     session_id=fields.Many2one('pos.session',string="Sesión")
    
#     cajero = fields.Many2one('res.users',related="session_id.user_id", string="Cajero"
#     )
    
    status=fields.Selection([
        ('01','Pendiente'),
        ('02','Retirado')
    ], string='Estatus Retiro', default=False, store=True)