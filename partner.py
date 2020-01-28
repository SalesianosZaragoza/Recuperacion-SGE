# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    bookseller = fields.Boolean("Active", default=False)

    session_ids = fields.Many2many('library.session',
        string="Sessions", readonly=True)
