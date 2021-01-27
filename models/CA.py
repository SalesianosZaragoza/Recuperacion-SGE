from odoo import models, fields, api

class CA(models.Model):
    _name = 'npi.CA'

    name = fields.Char(string="Name", required=True)