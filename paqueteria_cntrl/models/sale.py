from odoo import models, fields, api, _
import logging
import json
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
import datetime

class sale_order_inherit(models.Model):
    _inherit = 'sale.order'
    _description='Orden de venta'

    is_fragil=fields.Boolean(
        string="Fragil?",
        tracking=True,
    )

    contenido_paquete=fields.Char(
        string="Contenido de paquete",
        tracking=True,
    )
