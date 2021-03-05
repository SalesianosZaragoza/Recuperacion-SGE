from odoo import models, fields, api

class ca(models.Model):
    _name = 'npi.ca'

    name = fields.Char(string="Name", required=True)