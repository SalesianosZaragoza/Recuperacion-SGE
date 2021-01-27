from odoo import models, fields, api

class Species(models.Model):
    _name = 'npi.Species'

    name = fields.Char(string="Scientific name", required=True)
    name = fields.Char(string="Vulgar name", required=True)
    extension = fields.Integer(string="Extension", required=True)