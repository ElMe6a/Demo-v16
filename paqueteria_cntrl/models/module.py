from odoo import models, fields, api, tools, _
import logging
import datetime
from odoo.exceptions import Warning
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class ctrl_llantas(models.Model): 
    _name = "paqueteria_cntrl.monitor"
    _description = "Monitor"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(
        string="Nombre",
        tracking=True
    )



