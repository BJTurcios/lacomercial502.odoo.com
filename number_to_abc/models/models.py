# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCurrency(models.Model):
    _inherit = 'res.currency'
long_name = fields.Char(
        string='Nombre Completo',
    )
