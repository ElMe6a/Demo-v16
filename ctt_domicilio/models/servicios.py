# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, _
import logging
import datetime
from odoo.exceptions import Warning
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class ServDomicilio(models.Model):
    _name = "ctt_domicilio.registro"
    _description = "Registro"
    _order = "id desc"
    
    fecha = fields.Datetime(
        string="Fecha orden"
    )